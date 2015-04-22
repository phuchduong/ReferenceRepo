using System;
namespace Promotions.Repositories
{
    public interface IProductsRepository
    {
        System.Collections.Generic.IEnumerable<Product> GetProducts();

        System.Collections.Generic.IEnumerable<Product> GetRelatedProducts(Int64 productId);

        Product GetProduct(Int64 id);
    }
}
