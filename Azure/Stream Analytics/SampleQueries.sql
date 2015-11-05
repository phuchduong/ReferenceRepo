-- Purchases that happened within 1 minute of a click.
select
   Clicks.CustomerId,
   Clicks.ProductId,
   Clicks.ClickTime,
   Purchases.PurchaseTime
into output
from
   Clicks timestamp by ClickTime
   INNER JOIN Purchases Timestamp by PurchaseTime
   on Clicks.CustomerId = Purchases.CustomerId
   and Clicks.ProductId = Purchases.ProductId
   and Datediff(minute, Clicks, Purchases) Between -1 and 1

-- Find the customers who did not buy anything but clicked on a product.
select
   Clicks.CustomerId,
   Clicks.ProductId
   , System.Timestamp as ClickTime
   , Count(*) as Count
into output
from
   Clicks timestamp by ClickTime
   Left JOIN Purchases Timestamp by PurchaseTime
   on Clicks.CustomerId = Purchases.CustomerId
   and Clicks.ProductId = Purchases.ProductId
   and Datediff(minute, Clicks, Purchases) Between -1 and 1
Where
   Purchases.CustomerId is null
group by
   Clicks.CustomerId
   , Clicks.ProductID,
   SlidingWindow(minute, 1)

-- People who did not buy anything within 1 minute of a click, with more information.
select
    Clicks.CustomerId,
    Clicks.ProductId
    , System.Timestamp as ClickTime
    , Count(*) as Count
    , Products.Price
    , Promotions.Promotion
    , Promotions.Type
into output
from
    Clicks timestamp by ClickTime
    Left JOIN Purchases Timestamp by PurchaseTime
        on Clicks.CustomerId = Purchases.CustomerId
        and Clicks.ProductId = Purchases.ProductId
        and Datediff(minute, Clicks, Purchases) Between -1 and 1
    inner join Promotions
        on Clicks.ProductId = Promotions.ProductId
    inner join Products
        on Clicks.ProductId = Products.Id
Where
    Purchases.CustomerId is null
group by
    Clicks.CustomerId
    , Clicks.ProductID
    , SlidingWindow(minute, 1)
    , Products.Price
    , Promotions.Promotion
    , Promotions.Type

-- Who clicked a produce twice within 1 minute but did not buy anything.
select
    Clicks.CustomerId,
    Clicks.ProductId
    , System.Timestamp as ClickTime
    , Count(*) as Count
    , Products.Price
    , Promotions.Promotion
    , Promotions.Type
into output
from
    Clicks timestamp by ClickTime
    Left JOIN Purchases Timestamp by PurchaseTime
        on Clicks.CustomerId = Purchases.CustomerId
        and Clicks.ProductId = Purchases.ProductId
        and Datediff(minute, Clicks, Purchases) Between -1 and 1
    inner join Promotions
        on Clicks.ProductId = Promotions.ProductId
    inner join Products
        on Clicks.ProductId = Products.Id
Where
    Purchases.CustomerId is null
group by
    Clicks.CustomerId
    , Clicks.ProductID
    , SlidingWindow(minute, 1)
    , Products.Price
    , Promotions.Promotion
    , Promotions.Type
Having
    [count] >= 2

-- Computational Pricing. 
-- For those who not purchased an item after clicking on a product,
-- offer them a discount.
select
    Clicks.CustomerId,
    Clicks.ProductId,
    --Products.Price as OriginalPrice,
    
    -- compute the discount of the promotion
    case
        when Promotions.Type = '%' then Products.Price * (100 - Promotions.Promotion) / 100
        Else Products.Price - Promotions.Promotion
    end as NewPrice,
    Promotions.Promotion
    , count(*) as [Count]
into 
    output
from
    Clicks timestamp by ClickTime
    Left JOIN Purchases Timestamp by PurchaseTime
        on Clicks.CustomerId = Purchases.CustomerId
        and Clicks.ProductId = Purchases.ProductId
        and Datediff(minute, Clicks, Purchases) Between -1 and 1
    inner join Promotions
        on Clicks.ProductId = Promotions.ProductId
    inner join Products
        on Clicks.ProductId = Products.Id
Where
    Purchases.CustomerId is null
group by
    Clicks.CustomerId
    , Clicks.ProductID
    , SlidingWindow(minute, 1)
    , Products.Price
    , Promotions.Promotion
    , Promotions.Type
Having
    [count] >= 2

-- User click monitoring
SELECT
    Customers.Name AS Customer,
    Products.Name AS Product,
       Customers.Region,
    COUNT(*) AS Count,
    System.TimeStamp AS TimeStamp,
    'Click' AS Action
FROM
    Clicks TIMESTAMP BY clickTime
    INNER JOIN Products
    ON Clicks.ProductId = Products.Id
    INNER JOIN Customers
    ON Clicks.CustomerId = Customers.Id
GROUP BY
    TumblingWindow(minute, 1),
    Products.Name,
    Customers.Region,
    Customers.Name
 
      
      
      
SELECT
    Customers.Name AS Customer,
    Products.Name AS Product,
       Customers.Region,
    COUNT(*) AS Count,
    System.TimeStamp AS TimeStamp,
    'Purchase' AS Action
FROM
    Purchases TIMESTAMP BY purchaseTime
    INNER JOIN Products
    ON Purchases.ProductId = Products.Id
    INNER JOIN Customers
    ON Purchases.CustomerId = Customers.Id
GROUP BY
    TumblingWindow(minute, 1),
    Products.Name,
    Customers.Region,
    Customers.Name





SELECT
    System.timestamp as WindowEnd,
    card_type,
    count(*)
INTO
    blob
FROM
    creditstream timestamp by swipe_date
group by TumblingWindow(second, 15), card_type
;

SELECT
    swipe_date,
    transaction_id,
    card_type,
    user_gender,
    user_first_name,
    user_last_name,
    merchant,
    transaction_amount,
    balance,
    merchant_fee,
    swip_city_state as location
INTO
    CreditPowerBi
FROM
    CreditHub timestamp by swipe_date;
SELECT
    *
INTO
    SensorTagPowerBi
FROM
    SensorTagHub;
select
    created_at_iso as create_at,
    id_str as tweet_id,
    text as tweet_body,
    tweet_long_lat
INTO
    TwitterPowerBi
FROM
    TwitterHub;
SELECT
    timecreated as Time,
    displayname as DeviceName,
    measurename as MeasureUnit,
    value as Reading
INTO
    PiPowerBI
FROM
    PiHub timestamp by timecreated;