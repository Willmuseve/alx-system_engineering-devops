This is a README file for the 0x19- postmoterm project

It is an incident report about a working ecommerce app that returned error code 500 which affected almost 100% of the users.

Here is the report:


Issue Summary
Duration: 2024-01-21 15:30 EST to 16:45 EST (1 hour and 15 minutes)
Impact: Ecommerce web app returned error 500 for all users, preventing any purchases or access to account information. Approximately 100% of users were affected.
Root Cause: Unintended consequence of a recent database optimization script that resulted in a table lock.
Timeline
15:30 EST: Alert triggered for increased error 500 responses on the web app.
15:35 EST: Initial investigation focused on web servers and application logs, suspecting a code issue.
15:50 EST: Review of database logs revealed a table lock occurring since 15:28 EST.
16:00 EST: Incident escalated to DBA team for assistance.
16:15 EST: DBA identified the optimization script as the source of the lock and reverted the changes.
16:30 EST: Table lock released, app functionality restored.
16:45 EST: Monitoring confirmed full recovery and incident closed.
Root Cause and Resolution
Root Cause: A recently implemented database optimization script unintentionally caused a table lock, preventing the web app from accessing critical data.
Resolution: The DBA team reverted the script changes, releasing the lock and restoring app functionality.
Corrective and Preventative Measures
Improve Code Reviews: Implement a more rigorous code review process for database changes, including testing in a staging environment.
Enhanced Monitoring: Add alerts for table locks and database performance issues to enable proactive detection.
Thorough Testing: Conduct thorough testing of database changes in a non-production environment before deployment.
Specific Tasks
Review and update code review guidelines for database changes.
Implement monitoring for table locks and database performance metrics.
Establish a mandatory testing process for database changes in a staging environment.
Conduct a post-incident review to identify any additional contributing factors or areas for improvement.

