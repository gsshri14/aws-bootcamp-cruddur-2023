from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import db

# Honeycomb stuff
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
  #def run(logger):  
    # Just disabling to save spend on CloudWatch
    #logger.info('HomeActivities')
    # Honeycomb stuff
    #with tracer.start_as_current_span("home-activities-mock-data"):
      #span = trace.get_current_span()
      #now = datetime.now(timezone.utc).astimezone()
      #span.set_attribute("app.now", now.isoformat())

    sql = db.query_array_json('activities', 'home')
    results = db.query_array_json(sql)
    return results
       
