using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Configuration;
using Microsoft.ServiceBus.Messaging;
using Microsoft.WindowsAzure;



namespace ClickStreamDemo
{
    class Program
    {
        static void Main(string[] args)
        {
           
            string connectionString = CloudConfigurationManager.GetSetting("Microsoft.ServiceBus.ConnectionString");
            string clickEventHubName = CloudConfigurationManager.GetSetting("clickEvents");
            string purchaseEventHubName = CloudConfigurationManager.GetSetting("purchaseEvents");
            int numberOfMessages = int.Parse(CloudConfigurationManager.GetSetting("eventCount"));
            int numberOfMessagesVariance = int.Parse(CloudConfigurationManager.GetSetting("eventCountVariance"));

            numberOfMessages += new Random().Next(-numberOfMessagesVariance, numberOfMessagesVariance);

            Console.WriteLine(connectionString);
            Console.WriteLine(clickEventHubName);
            Console.WriteLine(purchaseEventHubName);
            Console.WriteLine(numberOfMessages);

            Sender s = new Sender(clickEventHubName, purchaseEventHubName, numberOfMessages);
            s.SendEvents();
            

            Console.WriteLine("Press enter key to stop worker.");
            Console.ReadLine();

        }

        

    }
}
