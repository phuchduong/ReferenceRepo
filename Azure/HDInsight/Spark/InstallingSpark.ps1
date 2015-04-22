New-AzureHDInsightClusterConfig -ClusterSizeInNodes $clusterNodes

     | Set-AzureHDInsightDefaultStorage -StorageAccountName $storageAccountName
-StorageAccountKey $storageAccountKey -StorageContainerName $containerName

     | Add-AzureHDInsightScriptAction -Name "Install Spark"
-ClusterRoleCollection HeadNode,DataNode
-Uri https://hdiconfigactions.blob.core.windows.net/sparkconfigactionv01/spark-installer-v01.ps1

     | New-AzureHDInsightCluster -Name $clusterName -Location $location