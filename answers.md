#### How long did you spend on the coding test below?
 I spent 64 hours on the coding test. 8hours daily for 8 days

#### What would you add to your solution if you had more time?

If I had more time on the coding challenge, I would add RabbitMQ in place of Django Signals for auto updating AuditLog table.
Because, Django signals is synchronous which cause some slight delay before a user get a response when changes are made on Favorites Table.  

#### What was the most useful feature that was added to the latest version of your chosen language? 

- #### Data Classes

One new in Python 3.7 is the data class. It is created using the new @dataclass decorator and using it we can safely create a call without __init__ method.
An example of a use case is shown below.

```import asyncio

@dataclass
class BackgroundTaskWorker:

    """
        Background worker class
    """

    @classmethod
    def start_work(cls, asyn_function, args):
        """This function helps to run an unpredictable function in the background.

        it uses an event loop as central executor.

        :param asyn_function: An asyn function that acts as coroutine.
        :param args: The async function args or params.
                     it should be a tuple of args.
        :return: None
        """
        event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(event_loop)
        event_loop.run_in_executor(None, cls.run_task, asyn_function, args)

    @classmethod
    def run_task(cls, asyn_function, args):
        """This function creates a future task which runs in background
        until completion

        :param asyn_function: An asyn function that acts as coroutine
        :param args: The async function args or params
        :return: None
        """
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        task = asyncio.ensure_future(asyn_function(*args))

        loop.run_until_complete(task)
        loop.close()
```

#### How would you track down a performance issue in production? Have you ever had to do this?
To track performance issue in production I use tools like sentry and runscope. Recently, I had some issue related to database 
connection pool in production. I was able to track the problem easily with 
sentry (Breadcrumbs, which is a trail of events which happened prior to an issue) and I resolved it easily


- Sentry is an open-source application monitoring platform that helps to identify issues in real-time. 
It's easy to setup and it's very useful for tracking errors and performance in production.

- Runscope is an API monitoring tool. Apart from the monitoring feature, It also helps to get visibility into API performance 
so as to can stay ahead of intermittent problems that could cause outages and it ensures that the structure and content of API calls 
are returning the expected data.
