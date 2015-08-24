Select
	T1Col1 as Review_Score,
	T1Col2 as Review_Text,
	(CASE
		WHEN T1Col1 < 3 THEN 'Negative'
		WHEN T1Col1 > 3 THEN 'Positive'
		ELSE 'Neutral'
		END
	) as Sentinment
from t1;