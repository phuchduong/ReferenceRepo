#You must run powershell in administrative mode.
#You must first enable scripts on your machine. Using: Set-ExecutionPolicy RemoteSigned
#Establish a connection to azure itself using: Add-AzureAccount to setup an instance based 12 session.

#Get the subscription file by calling: Get-AzurePublishSettingsFile
$subscriptionSettingsFile = "C:\Users\PhucHDuong\Documents\Data Mining\HDInsight Map Reduce Example\BizSpark.publishsettings"

Import-AzurePublishSettingsFile $subscriptionSettingsFile
Get-AzureSubscription
Select-AzureSubscription -SubscriptionName "BizSpark"

$subscriptionName = "BizSpark"
$storageAccountName = "dojosamplestorage"
$containerName = "dojosamplehadoopcluster"
$clusterName = "dojosamplehadoopcluster"
$queryString = "select * from titanic limit 100;"
$hiveJobDefinition = New-AzureHDInsightHiveJobDefinition -Query $queryString
Select-AzureSubscription $subscriptionName
$hiveJob = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $hiveJobDefinition
Wait-AzureHDInsightJob -Job $hiveJob -WaitTimeoutInSeconds 3600
Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $hiveJob.JobId -StandardOutput