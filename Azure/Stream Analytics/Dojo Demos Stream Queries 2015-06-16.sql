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
    created_at as tweet_date,
    id as tweet_id,
    text as tweet_body
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