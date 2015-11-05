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
$containerName = "dojosamplehadoop"
$clusterName = "dojosamplehadoop"

#uploads to https://dojosamplestorage.blob.core.windows.net/dojosamplecluster/iris.csv
$fileName ="C:\Users\PhucHDuong\Documents\Data Mining\HDInsight Map Reduce Example\iris.data.csv"
$blobName = "iris.csv"

# Get the storage account key
Select-AzureSubscription $subscriptionName
$storageaccountkey = get-azurestoragekey $storageAccountName | %{$_.Primary}

# Create the storage context object
$destContext = New-AzureStorageContext -StorageAccountName $storageAccountName -StorageAccountKey $storageaccountkey

# Copy the file from local workstation to the Blob container        
Set-AzureStorageBlobContent -File $fileName -Container $containerName -Blob $blobName -context $destContext