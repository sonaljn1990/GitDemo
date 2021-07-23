import unittest
from MakeMyTripProject.Tests.test_login import test_login
from MakeMyTripProject.Tests.test_FlightSearch import test_flightSearch

tc1 = unittest.TestLoader().loadTestsFromTestCase(test_login)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_flightSearch)

sanityTestSuit = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(sanityTestSuit)

