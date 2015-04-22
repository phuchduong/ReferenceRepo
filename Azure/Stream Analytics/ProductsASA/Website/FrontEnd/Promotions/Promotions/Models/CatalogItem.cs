using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Web;

namespace Promotions.Models
{
    public class CatalogItem
    {
        public Int64 Id;

        public string Name;

        public string Category;

        public int OriginalPrice;

        public int CurrentPrice;

        public string PromotionDiscount;

        public string Price
        {
            get
            {
                if (string.IsNullOrWhiteSpace(PromotionDiscount))
                {
                    return OriginalPrice.ToString();
                }

                return string.Format(CultureInfo.InvariantCulture, "{0} instead of ${1} ({2} off)", CurrentPrice, OriginalPrice, PromotionDiscount);
            }
        }
    }
}