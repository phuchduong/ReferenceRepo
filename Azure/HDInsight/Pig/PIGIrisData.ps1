#You must run powershell in administrative mode.
#You must first enable scripts on your machine. Using: Set-ExecutionPolicy RemoteSigned
#Establish a connection to azure itself using: Add-AzureAccount to setup an instance based 12 session.

#Get the subscription file by calling: Get-AzurePublishSettingsFile
$subscriptionSettingsFile = "C:\Users\PhucHDuong\Documents\Data Mining\HDInsight Map Reduce Example\BizSpark.publishsettings"

Import-AzurePublishSettingsFile $subscriptionSettingsFile
Get-AzureSubscription
Select-AzureSubscription -SubscriptionName "BizSpark"

#$storageAccountName = "dojosamplestorage"
#$containerName = "dojosamplehadoopcluster"
$statusFolder = "/tutorials/usepig/status"
$clusterName = "dojosamplehadoopcluster"

#$queryString = "describe hivesampletable;"
#$hiveJobDefinition = New-AzureHDInsightHiveJobDefinition -Query $queryString
#$hiveJob = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $hiveJobDefinition
#Wait-AzureHDInsightJob -Job $hiveJob -WaitTimeoutInSeconds 3600
#Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $hiveJob.JobId -StandardOutput

# Create the Pig job definition
$QueryString =  "titanic = LOAD 'wasb:///titanic.csv';"+
                "DUMP titanic;"

$pigJobDefinition = New-AzureHDInsightPigJobDefinition -Query $QueryString -StatusFolder $statusFolder 

# Submit the Pig job
Write-Host "Submit the Pig job ..." -ForegroundColor Green
$pigJob = Start-AzureHDInsightJob -Cluster $clusterName -JobDefinition $pigJobDefinition

# Wait for the Pig job to complete
Write-Host "Wait for the Pig job to complete ..." -ForegroundColor Green
Wait-AzureHDInsightJob -Job $pigJob -WaitTimeoutInSeconds 3600

# Print the standard error and the standard output of the Pig job.
Write-Host "Display the standard output ..." -ForegroundColor Green
Get-AzureHDInsightJobOutput -Cluster $clusterName -JobId $pigJob.JobId -StandardOutput