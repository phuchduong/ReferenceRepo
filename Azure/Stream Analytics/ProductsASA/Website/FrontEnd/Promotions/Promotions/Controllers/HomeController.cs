using Promotions.Events;
using Promotions.Models;
using Promotions.Repositories;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Promotions.Controllers
{
    public class HomeController : Controller
    {
        ICustomerRepository _customerRepository;
        IProductsRepository _productsRepository;
        IPromotionsRepository _promotionsRepository;
        private ITelemetryRepository _telemetryRepository;

        public HomeController(
            ICustomerRepository customerRepository, 
            IProductsRepository productsRepository, 
            IPromotionsRepository promotionsRepository,
            ITelemetryRepository telemetryRepository)
        {
            _customerRepository = customerRepository;
            _productsRepository = productsRepository;
            _promotionsRepository = promotionsRepository;
            _telemetryRepository = telemetryRepository;
        }

        public ActionResult Buy(Int64 id)
        {
            var customer = _customerRepository.GetCustomerByName(User.Identity.Name);
            var product = _productsRepository.GetProduct(id);
            var promotion = _promotionsRepository.GetPromotion(customer.Id, product.Id);

            var purchaseEvent = new PurchaseEvent
            {
                customerId = customer.Id,
                productId = id,
                price = promotion != null ? promotion.NewPrice : product.Price,
                purchaseTime = DateTime.Now,
                orderId = Guid.NewGuid()
            };

            _telemetryRepository.SendPurchase(purchaseEvent);

            System.Threading.Thread.Sleep(TimeSpan.FromSeconds(5));

            return new HttpStatusCodeResult(System.Net.HttpStatusCode.OK);
        }

        public ActionResult Details(Int64 id)
        {
            var product = _productsRepository.GetProduct(id);

            if(product == null)
            {
                return new HttpStatusCodeResult(System.Net.HttpStatusCode.NotFound);
            }

            var relatedProducts = _productsRepository.GetRelatedProducts(product.Id);
            var relatedCatalogItems = new List<CatalogItem>();
            
            IEnumerable<Promotion> promotions = null;
            Customer customer = null;

            if (User.Identity.IsAuthenticated)
            {
                customer = _customerRepository.GetCustomerByName(User.Identity.Name);
                promotions = _promotionsRepository.GetPromotions(customer.Id);

                var clickEvent = new ClickEvent
                {
                    clickTime = DateTime.Now,
                    customerId = customer.Id,
                    productId = product.Id
                };

                _telemetryRepository.SendClick(clickEvent);
            }

            foreach (var relatedProduct in relatedProducts.OrderBy(p => p.Name))
            {
                relatedCatalogItems.Add(ProductToCatalogItem(promotions, customer, relatedProduct));
            }

            return View(new CatalogItemDetailsModel(ProductToCatalogItem(promotions, customer, product), relatedCatalogItems));
        }

        private static CatalogItem ProductToCatalogItem(IEnumerable<Promotion> promotions, Customer customer, Product relatedProduct)
        {
            var catalogItem = new CatalogItem
            {
                Id = relatedProduct.Id,
                Name = relatedProduct.Name,
                OriginalPrice = relatedProduct.Price
            };

            var promotion = promotions != null && customer != null ? promotions.FirstOrDefault(p => p.CustomerId == customer.Id && p.ProductId == relatedProduct.Id) : null;
            if (promotion != null)
            {
                catalogItem.CurrentPrice = promotion.NewPrice;
                catalogItem.PromotionDiscount = promotion.PromotionDiscount;
            }
            return catalogItem;
        }

        public ActionResult Index()
        {
            var catalogItems = new List<CatalogItem>();
            var products = _productsRepository.GetProducts();

            IEnumerable<Promotion> promotions = null;
            Customer customer = null;


            if(User.Identity.IsAuthenticated)
            {
                customer = _customerRepository.GetCustomerByName(User.Identity.Name);
                promotions = _promotionsRepository.GetPromotions(customer.Id);
            }

            foreach(var product in products.OrderBy(p => p.Name))
            {
                catalogItems.Add(ProductToCatalogItem(promotions, customer, product));
            }

            var catalogModel = new CatalogModel(catalogItems);

            return View(catalogModel);
        }
    }
}