Never forget a test
Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not. Testing is executing a system in order to identify any gaps, errors, or missing requirements contrary to the actual requirements. This tutorial will give you a basic understanding of software testing, its types, methods, levels, and other related terminologies.

Code that is not tested can’t be trusted

Bad reputation
“Testing is Too Expensive”: Pay less for testing during software development => pay more for maintenance or correction later. Early testing saves both time and cost in many aspects. However, reducing the cost without testing may result in improper design of a software application, rendering the product useless.
“Testing is Time-Consuming”: Testing is never a time-consuming process. However diagnosing and fixing the errors identified during proper testing is a time-consuming but productive activity.
“Only Fully Developed Products are Tested”: No doubt, testing depends on the source code but reviewing requirements and developing test cases is independent from the developed code. However, iterative or incremental approaches to a development life cycle model may reduce the requirement of testing on the fully developed software.
“Complete Testing is Possible”: It becomes an issue when a client or tester thinks that complete testing is possible. It is possible that all paths have been tested by the team but occurrence of complete testing is never possible. There might be some scenarios that are never executed by the test team or the client during the software development life cycle and may be executed once the project has been deployed.
“A Tested Software is Bug-Free”: No one can claim with absolute certainty that a software application is 100% bug-free even if a tester with superb testing skills has tested the application.
“Testers are Responsible for Quality of Product”: It is a very common misinterpretation that only testers or the testing team should be responsible for product quality. Testers’ responsibilities include the identification of bugs to the stakeholders and then it is their decision whether they will fix the bug or release the software. Releasing the software at the time puts more pressure on the testers, as they will be blamed for any error.
“Test Automation should be used wherever possible to Reduce Time”: Yes, it is true that Test Automation reduces the testing time, but it is not possible to start test automation at any time during software development. Test automaton should be started when the software has been manually tested and is stable to some extent. Moreover, test automation can never be used if requirements keep changing.
Basic
This standard deals with the following aspects to determine the quality of a software application:

Quality model
External metrics
Internal metrics
Quality in use metrics
This standard presents some set of quality attributes for any software such as:

Functionality
Reliability
Usability
Efficiency
Maintainability
Portability
Functional Testing
This is a type of black-box testing that is based on the specifications of the software that is to be tested. The application is tested by providing input and then the results are examined that need to conform to the functionality it was intended for. Functional testing of a software is conducted on a complete, integrated system to evaluate the system’s compliance with its specified requirements.

There are five steps that are involved while testing an application for functionality:

The determination of the functionality that the intended application is meant to perform.
The creation of test data based on the specifications of the application.
The output based on the test data and the specifications of the application.
The writing of test scenarios and the execution of test cases.
The comparison of actual and expected results based on the executed test cases.
An effective testing practice will see the above steps applied to the testing policies of every organization and hence it will make sure that the organization maintains the strictest of standards when it comes to software quality.

Unit Testing
This type of testing is performed by developers before the setup is handed over to the testing team to formally execute the test cases. Unit testing is performed by the respective developers on the individual units of source code assigned areas. The developers use test data that is different from the test data of the quality assurance team.

The goal of unit testing is to isolate each part of the program and show that individual parts are correct in terms of requirements and functionality.

Limitations of Unit Testing:

Testing cannot catch each and every bug in an application. It is impossible to evaluate every execution path in every software application. The same is the case with unit testing.
There is a limit to the number of scenarios and test data that a developer can use to verify a source code. After having exhausted all the options, there is no choice but to stop unit testing and merge the code segment with other units.
Integration Testing
Integration testing is defined as the testing of combined parts of an application to determine if they function correctly. Integration testing can be done in two ways: Bottom-up integration testing and Top-down integration testing.

Bottom-up integration: This testing begins with unit testing, followed by tests of progressively higher-level combinations of units called modules or builds.
Top-down integration: In this testing, the highest-level modules are tested first and progressively, lower-level modules are tested thereafter.
In a comprehensive software development environment, bottom-up testing is usually done first, followed by top-down testing. The process concludes with multiple tests of the complete application, preferably in scenarios designed to mimic actual situations.

System Testing
System testing tests the system as a whole. Once all the components are integrated, the application as a whole is tested rigorously to see that it meets the specified Quality Standards. This type of testing is performed by a specialized testing team.

System testing is important because of the following reasons:

System testing is the first step in the Software Development Life Cycle, where the application is tested as a whole.
The application is tested thoroughly to verify that it meets the functional and technical specifications.
The application is tested in an environment that is very close to the production environment where the application will be deployed.
System testing enables us to test, verify, and validate both the business requirements as well as the application architecture.
Regression Testing
Whenever a change in a software application is made, it is quite possible that other areas within the application have been affected by this change. Regression testing is performed to verify that a fixed bug hasn’t resulted in another functionality or business rule violation. The intent of regression testing is to ensure that a change, such as a bug fix should not result in another fault being uncovered in the application.

Regression testing is important because of the following reasons:

Minimize the gaps in testing when an application with changes made has to be tested.
Testing the new changes to verify that the changes made did not affect any other area of the application.
Mitigates risks when regression testing is performed on the application.
Test coverage is increased without compromising timelines.
Increase speed to market the product.
Acceptance Testing
This is arguably the most important type of testing, as it is conducted by the Quality Assurance Team who will gauge whether the application meets the intended specifications and satisfies the client’s requirement. The QA team will have a set of pre-written scenarios and test cases that will be used to test the application.

More ideas will be shared about the application and more tests can be performed on it to gauge its accuracy and the reasons why the project was initiated. Acceptance tests are not only intended to point out simple spelling mistakes, cosmetic errors, or interface gaps, but also to point out any bugs in the application that will result in system crashes or major errors in the application.

By performing acceptance tests on an application, the testing team will deduce how the application will perform in production. There are also legal and contractual requirements for acceptance of the system.

Alpha Testing
This test is the first stage of testing and will be performed amongst the teams (developer and QA teams). Unit testing, integration testing and system testing when combined together is known as alpha testing. During this phase, the following aspects will be tested in the application:

Spelling Mistakes
Broken Links
Cloudy Directions
The Application will be tested on machines with the lowest specification to test loading times and any latency problems.
Beta Testing
This test is performed after alpha testing has been successfully performed. In beta testing, a sample of the intended audience tests the application. Beta testing is also known as pre-release testing. Beta test versions of software are ideally distributed to a wide audience on the Web, partly to give the program a “real-world” test and partly to provide a preview of the next release. In this phase, the audience will be testing the following:

Users will install, run the application and send their feedback to the project team.
Typographical errors, confusing application flow, and even crashes.
Getting the feedback, the project team can fix the problems before releasing the software to the actual users.
The more issues you fix that solve real user problems, the higher the quality of your application will be.
Having a higher-quality application when you release it to the general public will increase customer satisfaction.
Non-Functional Testing
This section is based upon testing an application from its non-functional attributes. Non-functional testing involves testing a software from the requirements which are nonfunctional in nature but important such as performance, security, user interface, etc.

Some of the important and commonly used non-functional testing types are discussed below.

Performance Testing
It is mostly used to identify any bottlenecks or performance issues rather than finding bugs in a software. There are different causes that contribute in lowering the performance of a software:

Network delay
Client-side processing
Database transaction processing
Load balancing between servers
Data rendering
Performance testing is considered as one of the important and mandatory testing type in terms of the following aspects:

Speed (i.e. Response Time, data rendering and accessing)
Capacity
Stability
Scalability
Performance testing can be either qualitative or quantitative and can be divided into different sub-types such as Load testing and Stress testing.

Load Testing
It is a process of testing the behavior of a software by applying maximum load in terms of software accessing and manipulating large input data. It can be done at both normal and peak load conditions. This type of testing identifies the maximum capacity of software and its behavior at peak time.

??? from here until ???END lines may have been inserted/deleted
Most of the time, load testing is performed with the help of automated tools such as Load Runner, AppLoader, IBM Rational Performance Tester, Apache JMeter, Silk Performer, Visual Studio Load Test, etc.

Virtual users (VUsers) are defined in the automated testing tool and the script is executed to verify the load testing for the software. The number of users can be increased or decreased concurrently or incrementally based upon the requirements.

Stress Testing
Stress testing includes testing the behavior of a software under abnormal conditions. For example, it may include taking away some resources or applying a load beyond the actual load limit.

The aim of stress testing is to test the software by applying the load to the system and taking over the resources used by the software to identify the breaking point. This testing can be performed by testing different scenarios such as:

Shutdown or restart of network ports randomly
Turning the database on or off
Running different processes that consume resources such as CPU, memory, server, etc.
Usability Testing
Usability testing is a black-box technique and is used to identify any error(s) and improvements in the software by observing the users through their usage and operation.

According to Nielsen, usability can be defined
???END
