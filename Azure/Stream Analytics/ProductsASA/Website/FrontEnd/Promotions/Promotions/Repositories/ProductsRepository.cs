using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Web;

namespace Promotions.Repositories
{
    public class ProductsRepository : IProductsRepository
    {
        Func<SqlConnection> _getConnection;

        public ProductsRepository(Func<SqlConnection> getConnection)
        {
            _getConnection = getConnection;
        }

        public IEnumerable<Product> GetProducts()
        {
            var products = new List<Product>();
            using (var conn = _getConnection())
            {
                conn.Open();
                using (var cmd = conn.CreateCommand())
                {
                    cmd.CommandText = "SELECT * FROM Products";
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            products.Add(
                                new Product
                                {
                                    Id = (Int64)reader["Id"],
                                    Name = reader["Name"].ToString(),
                                    Price = (int)reader["Price"]
                                });
                        }
                    }
                }
            }

            return products;
        }

        public Product GetProduct(Int64 id)
        {
            var products = new List<Product>();
            using (var conn = _getConnection())
            {
                conn.Open();
                using (var cmd = conn.CreateCommand())
                {
                    cmd.CommandText = "SELECT * FROM Products WHERE Id = @Id";
                    cmd.Parameters.Add(new SqlParameter("Id", System.Data.SqlDbType.BigInt) { Value = id });
                    using (var reader = cmd.ExecuteReader())
                    {
                        if (!reader.Read())
                        {
                            return null;
                        }

                        return new Product
                        {
                            Id = (Int64)reader["Id"],
                            Name = reader["Name"].ToString(),
                            Price = (int)reader["Price"]
                        };
                    }
                }
            }
        }

        public IEnumerable<Product> GetRelatedProducts(Int64 productId)
        {
            var products = new List<Product>();
            using (var conn = _getConnection())
            {
                conn.Open();
                using (var cmd = conn.CreateCommand())
                {
                    cmd.CommandText = "SELECT DISTINCT Products.Id, Products.Name, Products.Price FROM RelatedProducts AS Related INNER JOIN Products ON Related.RelatedProductId = Products.Id WHERE Related.ProductId = @ProductId";
                    cmd.Parameters.Add(new SqlParameter("ProductId", System.Data.SqlDbType.BigInt) { Value = productId });
                    using (var reader = cmd.ExecuteReader())
                    {
                        while (reader.Read())
                        {
                            products.Add(
                                new Product
                                {
                                    Id = (Int64)reader["Id"],
                                    Name = reader["Name"].ToString(),
                                    Price = (int)reader["Price"]
                                });
                        }
                    }
                }
            }

            return products;
        }


    }
}