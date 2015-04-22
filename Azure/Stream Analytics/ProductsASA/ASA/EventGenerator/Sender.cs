using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.ServiceBus.Messaging;
using Newtonsoft.Json;
using Microsoft.WindowsAzure;

namespace ClickStreamDemo
{
    class Sender
    {
        Int64[] products = new Int64[] {
            1726268,
            1872715,
            1908846,
            2107742,
            2151353,
            2168235,
            2192805,
            2199466,
            2305127,
            2325727,
            2344900
        };
        int customerCount = 50;
        string clickEventHubName;
        string purchaseEventHubName;
        int numberOfMessages;
        
        //Create Test JSON file for TStreams Use
        //System.IO.StreamWriter clicks = new System.IO.StreamWriter(@"C:\Users\zivk\Documents\Visual Studio 2013\Projects\BillGDemo\TestFiles\clickEvents.txt");
        //System.IO.StreamWriter purchases = new System.IO.StreamWriter(@"C:\Users\zivk\Documents\Visual Studio 2013\Projects\BillGDemo\TestFiles\purchaseEvents.txt");

        public Sender(string clickEventHubName, string purchaseEventHubName, int numberOfMessages)
        {
            this.clickEventHubName = clickEventHubName;
            this.purchaseEventHubName = purchaseEventHubName;
            this.numberOfMessages = numberOfMessages;
        }


        public void SendEvents()
        {
            // Create EventHubClient
            EventHubClient clickClient = EventHubClient.Create(this.clickEventHubName);
            EventHubClient purchaseClient = EventHubClient.Create(this.purchaseEventHubName);

            try
            {
                List<Task> tasks = new List<Task>();
                // Send messages to Event Hub
                Console.WriteLine("Sending click messages to Event Hub {0}", clickClient.Path);
                Console.WriteLine("Sending purchase messages to Event Hub {0}", purchaseClient.Path);
                Random random = new Random();


                //Create Test JSON file for TStreams Use
                //clicks.WriteLine("[");
                //purchases.WriteLine("[");
                
                // Maps a user and a product to how many times there was a view
                var userViews = new Dictionary<Tuple<Int64, Int64>, int>();

                // Maps a user to the products they purchase
                var userPurchases = new HashSet<Tuple<Int64, Int64>>();

                for (int i = 0; i < this.numberOfMessages; ++i)
                {
                    // Create the device/temperature metric
                    Int64 userId;
                    Int64 productId;
                    Tuple<Int64, Int64> key;
                    do
                    {
                        if (userPurchases.Count == products.Length * customerCount)
                        {
                            throw new InvalidOperationException("All users have purchased all products");
                        }
                        userId = random.Next(1, customerCount);
                        productId = products[random.Next(products.Length)];
                        key = new Tuple<Int64, Int64>(userId, productId);
                    } while (userPurchases.Contains(key));

                    tasks.Add(Click(clickClient, userId, productId));

                    if(!userViews.ContainsKey(key))
                    {
                        userViews[key] = 0;
                    }

                    userViews[key]++;

                    if(random.Next(10) == 0)
                    {
                        Purchase(purchaseClient, userId, productId, random);
                        userPurchases.Add(key);
                    }

                };

                Task.WaitAll(tasks.ToArray());
                //Create Test JSON file for TStreams Use
                //clicks.WriteLine("]");
                //clicks.Flush();
                //clicks.Close();
                //purchases.WriteLine("]");
                //purchases.Flush();
                //purchases.Close();
                Console.WriteLine("Finished waiting");
            }
            catch (Exception exp)
            {
                Console.WriteLine("Error on send: " + exp.Message);
            }
        }

        private Task Purchase(EventHubClient client, Int64 userId, Int64 productId, Random random)
        {
            var info = new PurchaseEvent() { productId = productId, customerId = userId, purchaseTime = DateTime.Now, orderId = Guid.NewGuid(), price = random.Next(10000) };
            var serializedString = JsonConvert.SerializeObject(info);
            EventData data = new EventData(Encoding.UTF8.GetBytes(serializedString))
            {
                PartitionKey = info.productId.ToString()
            };

            // Set user properties if needed
            data.Properties.Add("Type", "Telemetry_" + DateTime.Now.ToLongTimeString());
            //OutputMessageInfo("SENDING: ", data, info);

            Console.WriteLine("{0}: {1}", client.Path, serializedString);

            // Send the metric to Event Hub
            //purchases.Write("   ");
            //purchases.Write(serializedString);
            //purchases.WriteLine(",");
            //return Task.Factory.StartNew(() => { });
            
            return client.SendAsync(data);
        }

        private Task Click(EventHubClient client, Int64 userId, Int64 productId)
        {
            var info = new ClickEvent() { productId = productId, customerId = userId, clickTime = DateTime.Now };
            var serializedString = JsonConvert.SerializeObject(info);
            var data = new EventData(Encoding.UTF8.GetBytes(serializedString))
            {
                PartitionKey = info.productId.ToString()
            };

            // Set user properties if needed
            data.Properties.Add("Type", "Telemetry_" + DateTime.Now.ToLongTimeString());
            //OutputMessageInfo("SENDING: ", data, info);

            Console.WriteLine("{0}: {1}", client.Path, serializedString);

            //clicks.Write("   ");
            //clicks.Write(serializedString);
            //clicks.WriteLine(",");
            //return Task.Factory.StartNew(() => { });

            return client.SendAsync(data);
        }

        static void OutputMessageInfo(string action, EventData data, ClickEvent info)
        {
            if (data == null)
            {
                return;
            }
            if (info != null)
            {
                Console.WriteLine("{0}{1} - ProductId {2}, UserId {3}, Click Time {4}.", action, data, info.productId, info.customerId, info.clickTime);
            }
        }

        static void OutputMessageInfo(string action, EventData data, PurchaseEvent info)
        {
            if (data == null)
            {
                return;
            }
            if (info != null)
            {
                Console.WriteLine("{0}{1} - ProductId {2}, UserId {3}, Purchase Time {4}, Order Id {5}, Price {6}", action, data, info.productId, info.customerId, info.purchaseTime, info.orderId, info.price);
            }
        }
    }

    class ClickEvent
    {
        public Int64 customerId { get; set; }

        public Int64 productId { get; set; }

        public DateTime clickTime { get; set; }
    }

    class PurchaseEvent
    {
        public Int64 customerId { get; set; }

        public Int64 productId { get; set; }

        public Guid orderId { get; set; }

        public int price { get; set; }

        public DateTime purchaseTime { get; set; }
    }

    
}
