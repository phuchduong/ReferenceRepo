using Promotions.Repositories;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Promotions.Models
{
    public class CatalogModel
    {
        public IEnumerable<CatalogItem> _catalogItems;

        public CatalogModel(IEnumerable<CatalogItem> catalogItems)
        {
            _catalogItems = catalogItems;
        }



    }

}
