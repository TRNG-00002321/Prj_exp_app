package com.revature.e2e.runners;

import org.junit.platform.suite.api.*;
import io.cucumber.junit.platform.engine.Constants;

/**
 * Cucumber Test Runner
 * 

 * 
 * This class configures how Cucumber tests are executed.
 * The @Suite annotation makes this a JUnit Platform test suite.
 */
@Suite
@IncludeEngines("cucumber")
@SelectClasspathResource("features")
@ConfigurationParameter(key = Constants.GLUE_PROPERTY_NAME, value = "com.revature.e2e.steps")
@ConfigurationParameter(key = Constants.PLUGIN_PROPERTY_NAME, value = "pretty, io.qameta.allure.cucumber7jvm.AllureCucumber7Jvm")
@ConfigurationParameter(key = Constants.FILTER_TAGS_PROPERTY_NAME, value = "not @wip" // Exclude work in progress
                                                                                      // scenarios
)
public class TestRunner {
    /*
     * This class doesn't need any code - the annotations do all the work!
     * 
     * To run Cucumber tests:
     * - From IDE: Right-click this class and Run as JUnit Test
     * - From Maven: mvn test -Dtest=TestRunner
     * 
     * The test results will be:
     * 1. Printed to console (pretty format)
     * 2. Saved to Allure results directory for reporting
     */
}
