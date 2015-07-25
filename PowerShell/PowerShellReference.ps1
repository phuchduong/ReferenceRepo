########################### Begin  Azure Login ##########################################
# increase the cursor size
[Console]::CursorSize = 25

# shows cached azure subscriptions
Get-AzureSubscription

# Select from multiple subscriptions
Select-AzureSubscription

# Select azure subscription by subscription name
Select-AzureSubscription -SubscriptionName "DSDojo - Production"

########################### End Azure Login ############################################

########################### Begin Stream Analytics #####################################

# Accessing Stream Analytics commands
Switch-AzureMode AzureResourceManager

# Shows all stream analytics jobs on the subscription
Get-AzureStreamAnalyticsJob

# returns information about all the Stream Analytics jobs in the resource group 
# StreamAnalytics-Default-Central-US.
Get-AzureStreamAnalyticsJob -ResourceGroupName StreamAnalytics-Default-Central-US 

# returns information about the Stream Analytics job StreamingJob in the resource
# group StreamAnalytics-Default-Central-US.
Get-AzureStreamAnalyticsJob -ResourceGroupName StreamAnalytics-Default-Central-US -Name StreamingJob

# Lists all of the inputs that are defined in a specified Stream Analytics job, 
# or gets information about a specific input.
Get-AzureStreamAnalyticsInput -ResourceGroupName StreamAnalytics-Default-Central-US -JobName StreamingJob
# or
Get-AzureStreamAnalyticsInput -ResourceGroupName StreamAnalytics-Default-West-US -JobName demos


# get specific input from a stream analytics job
Get-AzureStreamAnalyticsInput -ResourceGroupName StreamAnalytics-Default-West-US -JobName demos -Name SensorTagHub

########################### End Stream Analytics ############################################