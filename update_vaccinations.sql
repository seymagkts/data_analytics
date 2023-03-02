Update country_vaccination_stats set (SELECT AVG(daily_vaccinations),country FROM country_vaccination_stats GROUP BY country) where daily_vaccinations=NULL
