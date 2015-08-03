using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.HBase.Client;
using org.apache.hadoop.hbase.rest.protobuf.generated;

namespace HBaseSDKTest
{
    class Program
    {
        static void Main(string[] args)
        {
            string clusterURL = "https://phucHBase.azurehdinsight.net";
            string hadoopUsername = "admin";
            string hadoopUserPassword = "DojoGuest123#";
            ClusterCredentials creds = new ClusterCredentials(new Uri(clusterURL), hadoopUsername, hadoopUserPassword);

            HBaseClient hbaseClient = new HBaseClient(creds);

            string hbaseClientString = hbaseClient.ToString();

            Console.WriteLine(hbaseClientString);

            string userInput = Console.ReadLine();
            
        }
    }
}
