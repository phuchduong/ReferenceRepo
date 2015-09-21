#You must run powershell in administrative mode.
#You must first enable scripts on your machine. Using: Set-ExecutionPolicy RemoteSigned
#Establish a connection to azure itself using: Add-AzureAccount to setup an instance based 12 session.

#Get the subscription file by calling: Get-AzurePublishSettingsFile
$subscriptionSettingsFile = "C:\Users\PhucHDuong\Documents\Data Mining\HDInsight Map Reduce Example\BizSpark.publishsettings"

Import-AzurePublishSettingsFile $subscriptionSettingsFile
Get-AzureSubscription
Select-AzureSubscription -SubscriptionName "BizSpark"

$clusterName = "dojosamplehadoopcluster"

#Defines a job.
$wordCountJobDefinition = New-AzureHDInsightMapReduceJobDefinition `
                            -JarFile "wasb:///example/jars/hadoop-mapreduce-examples.jar" `
                            -ClassName "wordcount" `
                            -Arguments "wasb:///example/data/gutenberg/davinci.txt", "wasb:///example/data/WorDcountOutput"

# Submits the job to the cluster.
$wordCountJob = Start-AzureHDInsightJob `
                    -Cluster $clusterName `
                    -JobDefinition $wordCountJobDefinition

# Checks the job completion
Wait-AzureHDInsightJob `
                    -Job $wordCountJob `
                    -waitTimeoutInSeconds 3600

# Check the output log or the error log.
Get-AzureHDInsightJobOutput `
                    -Cluster $clusterName `
                    -JobId $wordCountJob.JobId `
                    -StandardError