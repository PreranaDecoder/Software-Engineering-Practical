import unittest
import otp_prb


# from otp import generate_otp


class TestgenerateOTP(unittest.TestCase):

    def testcase1(self):
        size = 4

        #To Check Otp
        res = otp_prb.otp(4)
        self.assertEqual(len(res), size)

        #To Check email address for sender
        Email = otp_prb.emailsender
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        #To Check email address for reciver
        Email2 = otp_prb.emailreceiver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)



    def testcase2(self):
        size = 4

        # To Check Otp
        res = otp_prb.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = otp_prb.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

    def testcase3(self):
        size = 4

        # To Check Otp
        res = otp_prb.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = otp_prb.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        #To Check email address for reciver
        Email2 = otp_prb.emailreceiver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)

    def testcase4(self):
        size = 4

        # To Check Otp
        res = otp_prb.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = otp_prb.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        #To Check email address for reciver
        Email2 = otp_prb.emailreceiver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)


if __name__ == '__main__':

    unittest.main()