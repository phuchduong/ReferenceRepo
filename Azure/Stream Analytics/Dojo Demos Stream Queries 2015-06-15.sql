SELECT
    *
INTO
    CreditPowerBi
FROM
    CreditHub;
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
    RaspberryPiPowerBI
FROM
    PiHub timestamp by timecreated;