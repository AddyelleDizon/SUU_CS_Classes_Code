import sys
from Fraction import Fraction

already_printed_error = False
def test(expected, given):
    """ Print the result of a test. """
    global already_printed_error
    if already_printed_error == False:
        linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
        if expected == given:
            msg = "Test at line {0} ok.".format(linenum)
            print(msg)
        else:
            msg = ("\tTest at line {0} FAILED.".format(linenum))
            print(msg)
            print("\t\tExpected: "+ str(expected))
            print("\t\tGiven   : "+ str(given))
            print("\t\tTester only prints a single error per section - there may be more")
            already_printed_error = True

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    global already_printed_error
    print("Starting tests - only failed tests print unless you change that")
    #Add your tests here

    #Dr B's tests follow:
    print('testing get_num')
    already_printed_error = False
    test(197, Fraction(197, 725).get_num())
    test(382, Fraction(382, 121).get_num())
    test(842, Fraction(842, 719).get_num())
    test(827, Fraction(827, 783).get_num())
    test(224, Fraction(224, 171).get_num())
    test(878, Fraction(878, 761).get_num())
    test(508, Fraction(508, 429).get_num())
    test(992, Fraction(992, 127).get_num())
    test(956, Fraction(956, 223).get_num())
    test(47, Fraction(47, 48).get_num())
    test(433, Fraction(433, 170).get_num())
    test(54, Fraction(54, 13).get_num())
    test(434, Fraction(434, 299).get_num())
    test(907, Fraction(907, 937).get_num())
    test(1000, Fraction(1000, 269).get_num())
    test(188, Fraction(188, 643).get_num())
    test(65, Fraction(65, 86).get_num())
    test(311, Fraction(311, 589).get_num())
    test(266, Fraction(266, 101).get_num())
    test(59, Fraction(59, 240).get_num())
    print('testing get_den')
    already_printed_error = False
    test(290, Fraction(193, 290).get_den())
    test(213, Fraction(824, 213).get_den())
    test(997, Fraction(147, 997).get_den())
    test(591, Fraction(455, 591).get_den())
    test(21, Fraction(533, 21).get_den())
    test(321, Fraction(22, 321).get_den())
    test(323, Fraction(791, 323).get_den())
    test(183, Fraction(214, 183).get_den())
    test(291, Fraction(449, 291).get_den())
    test(40, Fraction(491, 40).get_den())
    test(156, Fraction(37, 156).get_den())
    test(237, Fraction(904, 237).get_den())
    test(689, Fraction(83, 689).get_den())
    test(101, Fraction(304, 101).get_den())
    test(349, Fraction(142, 349).get_den())
    test(24, Fraction(103, 24).get_den())
    test(91, Fraction(526, 91).get_den())
    test(4, Fraction(9, 4).get_den())
    test(838, Fraction(769, 838).get_den())
    test(283, Fraction(100, 283).get_den())
    print('testing constructor for reduction')
    already_printed_error = False
    test(194, Fraction(194, 197).get_num())
    test(197, Fraction(4462, 4531).get_den())
    test(312, Fraction(312, 167).get_num())
    test(167, Fraction(23088, 12358).get_den())
    test(287, Fraction(287, 55).get_num())
    test(55, Fraction(257152, 49280).get_den())
    test(305, Fraction(305, 387).get_num())
    test(387, Fraction(35380, 44892).get_den())
    test(32, Fraction(32, 329).get_num())
    test(329, Fraction(21760, 223720).get_den())
    test(424, Fraction(424, 889).get_num())
    test(889, Fraction(178504, 374269).get_den())
    test(56, Fraction(56, 169).get_num())
    test(169, Fraction(55440, 167310).get_den())
    test(211, Fraction(211, 608).get_num())
    test(608, Fraction(82501, 237728).get_den())
    test(31, Fraction(31, 47).get_num())
    test(47, Fraction(12400, 18800).get_den())
    test(289, Fraction(289, 372).get_num())
    test(372, Fraction(29189, 37572).get_den())
    test(853, Fraction(853, 454).get_num())
    test(454, Fraction(571510, 304180).get_den())
    test(964, Fraction(964, 983).get_num())
    test(983, Fraction(573580, 584885).get_den())
    test(544, Fraction(544, 1009).get_num())
    test(1009, Fraction(382432, 709327).get_den())
    test(89, Fraction(89, 97).get_num())
    test(97, Fraction(73959, 80607).get_den())
    test(161, Fraction(161, 125).get_num())
    test(125, Fraction(153916, 119500).get_den())
    test(181, Fraction(181, 780).get_num())
    test(780, Fraction(55567, 239460).get_den())
    test(86, Fraction(86, 31).get_num())
    test(31, Fraction(59770, 21545).get_den())
    test(218, Fraction(218, 43).get_num())
    test(43, Fraction(155652, 30702).get_den())
    test(382, Fraction(382, 885).get_num())
    test(885, Fraction(372068, 861990).get_den())
    test(302, Fraction(302, 271).get_num())
    test(271, Fraction(11476, 10298).get_den())
    print('testing constructor for type checking')
    already_printed_error = False
    try:
        a = Fraction('diamond', 691)
        a = Fraction(287, 'Aristophanes')
        a = Fraction('accolade', 'massiveness')
        a = Fraction(0.082, 691)
        a = Fraction(287, 0.063)
        a = Fraction(0.067, 0.077)
        a = Fraction(True, 691)
        a = Fraction(287, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('unsymmetrical', 39)
        a = Fraction(235, 'demolition')
        a = Fraction('Nile', 'Riddle')
        a = Fraction(0.086, 39)
        a = Fraction(235, 0.057)
        a = Fraction(0.097, 0.09)
        a = Fraction(True, 39)
        a = Fraction(235, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('Hegel', 467)
        a = Fraction(268, 'mattress')
        a = Fraction('Clement', 'eaten')
        a = Fraction(0.081, 467)
        a = Fraction(268, 0.088)
        a = Fraction(0.013, 0.092)
        a = Fraction(True, 467)
        a = Fraction(268, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('undertake', 217)
        a = Fraction(162, 'breastfeed')
        a = Fraction('mustachio', 'PBS')
        a = Fraction(0.012, 217)
        a = Fraction(162, 0.092)
        a = Fraction(0.049, 0.006)
        a = Fraction(True, 217)
        a = Fraction(162, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('everything', 183)
        a = Fraction(131, 'Melchizedek')
        a = Fraction('swatting', 'gritter')
        a = Fraction(0.023, 183)
        a = Fraction(131, 0.027)
        a = Fraction(0.028, 0.001)
        a = Fraction(True, 183)
        a = Fraction(131, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('rectangle', 155)
        a = Fraction(327, 'sci')
        a = Fraction('leisurewear', 'misinformation')
        a = Fraction(0.024, 155)
        a = Fraction(327, 0.072)
        a = Fraction(0.052, 0.098)
        a = Fraction(True, 155)
        a = Fraction(327, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('theosophical', 328)
        a = Fraction(183, 'material')
        a = Fraction('plateful', 'lipid')
        a = Fraction(0.026, 328)
        a = Fraction(183, 0.019)
        a = Fraction(0.033, 0.03)
        a = Fraction(True, 328)
        a = Fraction(183, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('paycheck', 539)
        a = Fraction(130, 'wale')
        a = Fraction('studbook', 'triumvir')
        a = Fraction(0.076, 539)
        a = Fraction(130, 0.01)
        a = Fraction(0.095, 0.049)
        a = Fraction(True, 539)
        a = Fraction(130, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('Dionysus', 447)
        a = Fraction(13, 'rigorousness')
        a = Fraction('noxious', 'Britannic')
        a = Fraction(0.057, 447)
        a = Fraction(13, 0.037)
        a = Fraction(0.038, 0.002)
        a = Fraction(True, 447)
        a = Fraction(13, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    try:
        a = Fraction('kingfisher', 99)
        a = Fraction(20, 'virtuousness')
        a = Fraction('sysadmin', 'collectivist')
        a = Fraction(0.024, 99)
        a = Fraction(20, 0.045)
        a = Fraction(0.091, 0.087)
        a = Fraction(True, 99)
        a = Fraction(20, False)
        a = Fraction(False,True)
        test('TypeError','no error')
    except TypeError as err:
        test(True,True)
    print('testing - (subtract)')
    already_printed_error = False
    a = Fraction(7, 99)
    b = Fraction(861, 646)
    c = a - b
    try:
        test(-80717, c.get_num())
        test(63954, c.get_den())
    except AttributeError as err:
        test(-80717,c) 
    a = Fraction(167, 265)
    b = Fraction(151, 106)
    c = a - b
    try:
        test(-421, c.get_num())
        test(530, c.get_den())
    except AttributeError as err:
        test(-421,c) 
    a = Fraction(321, 797)
    b = Fraction(731, 308)
    c = a - b
    try:
        test(-483739, c.get_num())
        test(245476, c.get_den())
    except AttributeError as err:
        test(-483739,c) 
    a = Fraction(101, 5)
    b = Fraction(847, 937)
    c = a - b
    try:
        test(90402, c.get_num())
        test(4685, c.get_den())
    except AttributeError as err:
        test(90402,c) 
    a = Fraction(544, 279)
    b = Fraction(391, 606)
    c = a - b
    try:
        test(73525, c.get_num())
        test(56358, c.get_den())
    except AttributeError as err:
        test(73525,c) 
    a = Fraction(276, 181)
    b = Fraction(570, 637)
    c = a - b
    try:
        test(72642, c.get_num())
        test(115297, c.get_den())
    except AttributeError as err:
        test(72642,c) 
    a = Fraction(605, 388)
    b = Fraction(953, 439)
    c = a - b
    try:
        test(-104169, c.get_num())
        test(170332, c.get_den())
    except AttributeError as err:
        test(-104169,c) 
    a = Fraction(350, 1003)
    b = Fraction(820, 931)
    c = a - b
    try:
        test(-496610, c.get_num())
        test(933793, c.get_den())
    except AttributeError as err:
        test(-496610,c) 
    a = Fraction(5, 14)
    b = Fraction(655, 694)
    c = a - b
    try:
        test(-1425, c.get_num())
        test(2429, c.get_den())
    except AttributeError as err:
        test(-1425,c) 
    a = Fraction(527, 205)
    b = Fraction(387, 427)
    c = a - b
    try:
        test(145694, c.get_num())
        test(87535, c.get_den())
    except AttributeError as err:
        test(145694,c) 
    a = Fraction(936, 389)
    b = Fraction(301, 78)
    c = a - b
    try:
        test(-44081, c.get_num())
        test(30342, c.get_den())
    except AttributeError as err:
        test(-44081,c) 
    a = Fraction(608, 391)
    b = Fraction(451, 27)
    c = a - b
    try:
        test(-159925, c.get_num())
        test(10557, c.get_den())
    except AttributeError as err:
        test(-159925,c) 
    a = Fraction(103, 40)
    b = Fraction(769, 642)
    c = a - b
    try:
        test(17683, c.get_num())
        test(12840, c.get_den())
    except AttributeError as err:
        test(17683,c) 
    a = Fraction(347, 302)
    b = Fraction(780, 623)
    c = a - b
    try:
        test(-19379, c.get_num())
        test(188146, c.get_den())
    except AttributeError as err:
        test(-19379,c) 
    a = Fraction(215, 802)
    b = Fraction(801, 571)
    c = a - b
    try:
        test(-519637, c.get_num())
        test(457942, c.get_den())
    except AttributeError as err:
        test(-519637,c) 
    a = Fraction(356, 155)
    b = Fraction(813, 254)
    c = a - b
    try:
        test(-35591, c.get_num())
        test(39370, c.get_den())
    except AttributeError as err:
        test(-35591,c) 
    a = Fraction(671, 653)
    b = Fraction(379, 387)
    c = a - b
    try:
        test(12190, c.get_num())
        test(252711, c.get_den())
    except AttributeError as err:
        test(12190,c) 
    a = Fraction(335, 544)
    b = Fraction(334, 231)
    c = a - b
    try:
        test(-104311, c.get_num())
        test(125664, c.get_den())
    except AttributeError as err:
        test(-104311,c) 
    a = Fraction(109, 49)
    b = Fraction(217, 550)
    c = a - b
    try:
        test(49317, c.get_num())
        test(26950, c.get_den())
    except AttributeError as err:
        test(49317,c) 
    a = Fraction(69, 229)
    b = Fraction(33, 35)
    c = a - b
    try:
        test(-5142, c.get_num())
        test(8015, c.get_den())
    except AttributeError as err:
        test(-5142,c) 
    print('testing * (multiply)')
    already_printed_error = False
    a = Fraction(80, 79)
    b = Fraction(134, 3)
    c = a * b
    try:
        test(10720, c.get_num())
        test(237, c.get_den())
    except AttributeError as err:
        test(10720,c) 
    a = Fraction(12, 995)
    b = Fraction(311, 110)
    c = a * b
    try:
        test(1866, c.get_num())
        test(54725, c.get_den())
    except AttributeError as err:
        test(1866,c) 
    a = Fraction(19, 23)
    b = Fraction(13, 14)
    c = a * b
    try:
        test(247, c.get_num())
        test(322, c.get_den())
    except AttributeError as err:
        test(247,c) 
    a = Fraction(661, 238)
    b = Fraction(430, 207)
    c = a * b
    try:
        test(142115, c.get_num())
        test(24633, c.get_den())
    except AttributeError as err:
        test(142115,c) 
    a = Fraction(3, 5)
    b = Fraction(239, 405)
    c = a * b
    try:
        test(239, c.get_num())
        test(675, c.get_den())
    except AttributeError as err:
        test(239,c) 
    a = Fraction(889, 806)
    b = Fraction(698, 325)
    c = a * b
    try:
        test(310261, c.get_num())
        test(130975, c.get_den())
    except AttributeError as err:
        test(310261,c) 
    a = Fraction(425, 396)
    b = Fraction(640, 661)
    c = a * b
    try:
        test(68000, c.get_num())
        test(65439, c.get_den())
    except AttributeError as err:
        test(68000,c) 
    a = Fraction(14, 811)
    b = Fraction(261, 307)
    c = a * b
    try:
        test(3654, c.get_num())
        test(248977, c.get_den())
    except AttributeError as err:
        test(3654,c) 
    a = Fraction(318, 115)
    b = Fraction(694, 933)
    c = a * b
    try:
        test(73564, c.get_num())
        test(35765, c.get_den())
    except AttributeError as err:
        test(73564,c) 
    a = Fraction(172, 23)
    b = Fraction(67, 390)
    c = a * b
    try:
        test(5762, c.get_num())
        test(4485, c.get_den())
    except AttributeError as err:
        test(5762,c) 
    a = Fraction(199, 186)
    b = Fraction(789, 805)
    c = a * b
    try:
        test(52337, c.get_num())
        test(49910, c.get_den())
    except AttributeError as err:
        test(52337,c) 
    a = Fraction(333, 44)
    b = Fraction(191, 807)
    c = a * b
    try:
        test(21201, c.get_num())
        test(11836, c.get_den())
    except AttributeError as err:
        test(21201,c) 
    a = Fraction(941, 151)
    b = Fraction(877, 963)
    c = a * b
    try:
        test(825257, c.get_num())
        test(145413, c.get_den())
    except AttributeError as err:
        test(825257,c) 
    a = Fraction(75, 68)
    b = Fraction(212, 649)
    c = a * b
    try:
        test(3975, c.get_num())
        test(11033, c.get_den())
    except AttributeError as err:
        test(3975,c) 
    a = Fraction(25, 12)
    b = Fraction(638, 525)
    c = a * b
    try:
        test(319, c.get_num())
        test(126, c.get_den())
    except AttributeError as err:
        test(319,c) 
    a = Fraction(1003, 548)
    b = Fraction(32, 693)
    c = a * b
    try:
        test(8024, c.get_num())
        test(94941, c.get_den())
    except AttributeError as err:
        test(8024,c) 
    a = Fraction(24, 23)
    b = Fraction(813, 410)
    c = a * b
    try:
        test(9756, c.get_num())
        test(4715, c.get_den())
    except AttributeError as err:
        test(9756,c) 
    a = Fraction(216, 169)
    b = Fraction(662, 75)
    c = a * b
    try:
        test(47664, c.get_num())
        test(4225, c.get_den())
    except AttributeError as err:
        test(47664,c) 
    a = Fraction(955, 334)
    b = Fraction(263, 921)
    c = a * b
    try:
        test(251165, c.get_num())
        test(307614, c.get_den())
    except AttributeError as err:
        test(251165,c) 
    a = Fraction(340, 231)
    b = Fraction(8, 5)
    c = a * b
    try:
        test(544, c.get_num())
        test(231, c.get_den())
    except AttributeError as err:
        test(544,c) 
    print('testing / (divide)')
    already_printed_error = False
    a = Fraction(78, 311)
    b = Fraction(261, 497)
    c = a / b
    try:
        test(12922, c.get_num())
        test(27057, c.get_den())
    except AttributeError as err:
        test(12922,c) 
    a = Fraction(406, 321)
    b = Fraction(458, 335)
    c = a / b
    try:
        test(68005, c.get_num())
        test(73509, c.get_den())
    except AttributeError as err:
        test(68005,c) 
    a = Fraction(716, 663)
    b = Fraction(443, 400)
    c = a / b
    try:
        test(286400, c.get_num())
        test(293709, c.get_den())
    except AttributeError as err:
        test(286400,c) 
    a = Fraction(381, 44)
    b = Fraction(1008, 575)
    c = a / b
    try:
        test(73025, c.get_num())
        test(14784, c.get_den())
    except AttributeError as err:
        test(73025,c) 
    a = Fraction(43, 202)
    b = Fraction(324, 647)
    c = a / b
    try:
        test(27821, c.get_num())
        test(65448, c.get_den())
    except AttributeError as err:
        test(27821,c) 
    a = Fraction(959, 614)
    b = Fraction(548, 291)
    c = a / b
    try:
        test(2037, c.get_num())
        test(2456, c.get_den())
    except AttributeError as err:
        test(2037,c) 
    a = Fraction(261, 218)
    b = Fraction(247, 119)
    c = a / b
    try:
        test(31059, c.get_num())
        test(53846, c.get_den())
    except AttributeError as err:
        test(31059,c) 
    a = Fraction(38, 963)
    b = Fraction(174, 41)
    c = a / b
    try:
        test(779, c.get_num())
        test(83781, c.get_den())
    except AttributeError as err:
        test(779,c) 
    a = Fraction(631, 236)
    b = Fraction(387, 589)
    c = a / b
    try:
        test(371659, c.get_num())
        test(91332, c.get_den())
    except AttributeError as err:
        test(371659,c) 
    a = Fraction(59, 866)
    b = Fraction(92, 603)
    c = a / b
    try:
        test(35577, c.get_num())
        test(79672, c.get_den())
    except AttributeError as err:
        test(35577,c) 
    a = Fraction(10, 3)
    b = Fraction(73, 127)
    c = a / b
    try:
        test(1270, c.get_num())
        test(219, c.get_den())
    except AttributeError as err:
        test(1270,c) 
    a = Fraction(94, 791)
    b = Fraction(68, 79)
    c = a / b
    try:
        test(3713, c.get_num())
        test(26894, c.get_den())
    except AttributeError as err:
        test(3713,c) 
    a = Fraction(31, 408)
    b = Fraction(37, 556)
    c = a / b
    try:
        test(4309, c.get_num())
        test(3774, c.get_den())
    except AttributeError as err:
        test(4309,c) 
    a = Fraction(547, 427)
    b = Fraction(745, 928)
    c = a / b
    try:
        test(507616, c.get_num())
        test(318115, c.get_den())
    except AttributeError as err:
        test(507616,c) 
    a = Fraction(574, 99)
    b = Fraction(338, 155)
    c = a / b
    try:
        test(44485, c.get_num())
        test(16731, c.get_den())
    except AttributeError as err:
        test(44485,c) 
    a = Fraction(892, 803)
    b = Fraction(238, 955)
    c = a / b
    try:
        test(425930, c.get_num())
        test(95557, c.get_den())
    except AttributeError as err:
        test(425930,c) 
    a = Fraction(942, 479)
    b = Fraction(319, 689)
    c = a / b
    try:
        test(649038, c.get_num())
        test(152801, c.get_den())
    except AttributeError as err:
        test(649038,c) 
    a = Fraction(57, 191)
    b = Fraction(221, 439)
    c = a / b
    try:
        test(25023, c.get_num())
        test(42211, c.get_den())
    except AttributeError as err:
        test(25023,c) 
    a = Fraction(225, 206)
    b = Fraction(214, 279)
    c = a / b
    try:
        test(62775, c.get_num())
        test(44084, c.get_den())
    except AttributeError as err:
        test(62775,c) 
    a = Fraction(435, 104)
    b = Fraction(676, 225)
    c = a / b
    try:
        test(97875, c.get_num())
        test(70304, c.get_den())
    except AttributeError as err:
        test(97875,c) 
    print('testing >')
    already_printed_error = False
    a = Fraction(1, 110)
    b = Fraction(2, 110)
    c = a > b
    test(False,c) 
    a = Fraction(3, 80)
    b = Fraction(4, 80)
    c = a > b
    test(False,c) 
    a = Fraction(5, 70)
    b = Fraction(6, 70)
    c = a > b
    test(False,c) 
    a = Fraction(7, 120)
    b = Fraction(8, 120)
    c = a > b
    test(False,c) 
    a = Fraction(9, 200)
    b = Fraction(9, 200)
    c = a > b
    test(False,c) 
    a = Fraction(8, 20)
    b = Fraction(7, 20)
    c = a > b
    test(True,c) 
    a = Fraction(6, 170)
    b = Fraction(5, 170)
    c = a > b
    test(True,c) 
    a = Fraction(4, 60)
    b = Fraction(3, 60)
    c = a > b
    test(True,c) 
    a = Fraction(2, 130)
    b = Fraction(5, 130)
    c = a > b
    test(False,c) 
    a = Fraction(8, 10)
    b = Fraction(1, 10)
    c = a > b
    test(True,c) 
    a = Fraction(1, 40)
    b = Fraction(2, 40)
    c = a > b
    test(False,c) 
    a = Fraction(3, 40)
    b = Fraction(4, 40)
    c = a > b
    test(False,c) 
    a = Fraction(5, 90)
    b = Fraction(6, 90)
    c = a > b
    test(False,c) 
    a = Fraction(7, 170)
    b = Fraction(8, 170)
    c = a > b
    test(False,c) 
    a = Fraction(9, 130)
    b = Fraction(9, 130)
    c = a > b
    test(False,c) 
    a = Fraction(8, 30)
    b = Fraction(7, 30)
    c = a > b
    test(True,c) 
    a = Fraction(6, 80)
    b = Fraction(5, 80)
    c = a > b
    test(True,c) 
    a = Fraction(4, 20)
    b = Fraction(3, 20)
    c = a > b
    test(True,c) 
    a = Fraction(2, 140)
    b = Fraction(5, 140)
    c = a > b
    test(False,c) 
    a = Fraction(8, 10)
    b = Fraction(1, 10)
    c = a > b
    test(True,c) 
    print('testing >=')
    already_printed_error = False
    a = Fraction(1, 30)
    b = Fraction(2, 30)
    c = a >= b
    test(False,c) 
    a = Fraction(3, 40)
    b = Fraction(4, 40)
    c = a >= b
    test(False,c) 
    a = Fraction(5, 110)
    b = Fraction(6, 110)
    c = a >= b
    test(False,c) 
    a = Fraction(7, 180)
    b = Fraction(8, 180)
    c = a >= b
    test(False,c) 
    a = Fraction(9, 20)
    b = Fraction(9, 20)
    c = a >= b
    test(True,c) 
    a = Fraction(8, 150)
    b = Fraction(7, 150)
    c = a >= b
    test(True,c) 
    a = Fraction(6, 10)
    b = Fraction(5, 10)
    c = a >= b
    test(True,c) 
    a = Fraction(4, 140)
    b = Fraction(3, 140)
    c = a >= b
    test(True,c) 
    a = Fraction(2, 30)
    b = Fraction(5, 30)
    c = a >= b
    test(False,c) 
    a = Fraction(8, 70)
    b = Fraction(1, 70)
    c = a >= b
    test(True,c) 
    a = Fraction(1, 180)
    b = Fraction(2, 180)
    c = a >= b
    test(False,c) 
    a = Fraction(3, 70)
    b = Fraction(4, 70)
    c = a >= b
    test(False,c) 
    a = Fraction(5, 140)
    b = Fraction(6, 140)
    c = a >= b
    test(False,c) 
    a = Fraction(7, 70)
    b = Fraction(8, 70)
    c = a >= b
    test(False,c) 
    a = Fraction(9, 20)
    b = Fraction(9, 20)
    c = a >= b
    test(True,c) 
    a = Fraction(8, 160)
    b = Fraction(7, 160)
    c = a >= b
    test(True,c) 
    a = Fraction(6, 60)
    b = Fraction(5, 60)
    c = a >= b
    test(True,c) 
    a = Fraction(4, 180)
    b = Fraction(3, 180)
    c = a >= b
    test(True,c) 
    a = Fraction(2, 100)
    b = Fraction(5, 100)
    c = a >= b
    test(False,c) 
    a = Fraction(8, 60)
    b = Fraction(1, 60)
    c = a >= b
    test(True,c) 
    print('testing <')
    already_printed_error = False
    a = Fraction(1, 90)
    b = Fraction(2, 90)
    c = a < b
    test(True,c) 
    a = Fraction(3, 90)
    b = Fraction(4, 90)
    c = a < b
    test(True,c) 
    a = Fraction(5, 120)
    b = Fraction(6, 120)
    c = a < b
    test(True,c) 
    a = Fraction(7, 170)
    b = Fraction(8, 170)
    c = a < b
    test(True,c) 
    a = Fraction(9, 120)
    b = Fraction(9, 120)
    c = a < b
    test(False,c) 
    a = Fraction(8, 30)
    b = Fraction(7, 30)
    c = a < b
    test(False,c) 
    a = Fraction(6, 20)
    b = Fraction(5, 20)
    c = a < b
    test(False,c) 
    a = Fraction(4, 10)
    b = Fraction(3, 10)
    c = a < b
    test(False,c) 
    a = Fraction(2, 30)
    b = Fraction(5, 30)
    c = a < b
    test(True,c) 
    a = Fraction(8, 140)
    b = Fraction(1, 140)
    c = a < b
    test(False,c) 
    a = Fraction(1, 120)
    b = Fraction(2, 120)
    c = a < b
    test(True,c) 
    a = Fraction(3, 60)
    b = Fraction(4, 60)
    c = a < b
    test(True,c) 
    a = Fraction(5, 120)
    b = Fraction(6, 120)
    c = a < b
    test(True,c) 
    a = Fraction(7, 190)
    b = Fraction(8, 190)
    c = a < b
    test(True,c) 
    a = Fraction(9, 80)
    b = Fraction(9, 80)
    c = a < b
    test(False,c) 
    a = Fraction(8, 170)
    b = Fraction(7, 170)
    c = a < b
    test(False,c) 
    a = Fraction(6, 150)
    b = Fraction(5, 150)
    c = a < b
    test(False,c) 
    a = Fraction(4, 10)
    b = Fraction(3, 10)
    c = a < b
    test(False,c) 
    a = Fraction(2, 150)
    b = Fraction(5, 150)
    c = a < b
    test(True,c) 
    a = Fraction(8, 170)
    b = Fraction(1, 170)
    c = a < b
    test(False,c) 
    print('testing <=')
    already_printed_error = False
    a = Fraction(1, 90)
    b = Fraction(2, 90)
    c = a <= b
    test(True,c) 
    a = Fraction(3, 40)
    b = Fraction(4, 40)
    c = a <= b
    test(True,c) 
    a = Fraction(5, 190)
    b = Fraction(6, 190)
    c = a <= b
    test(True,c) 
    a = Fraction(7, 170)
    b = Fraction(8, 170)
    c = a <= b
    test(True,c) 
    a = Fraction(9, 10)
    b = Fraction(9, 10)
    c = a <= b
    test(True,c) 
    a = Fraction(8, 190)
    b = Fraction(7, 190)
    c = a <= b
    test(False,c) 
    a = Fraction(6, 40)
    b = Fraction(5, 40)
    c = a <= b
    test(False,c) 
    a = Fraction(4, 30)
    b = Fraction(3, 30)
    c = a <= b
    test(False,c) 
    a = Fraction(2, 80)
    b = Fraction(5, 80)
    c = a <= b
    test(True,c) 
    a = Fraction(8, 70)
    b = Fraction(1, 70)
    c = a <= b
    test(False,c) 
    a = Fraction(1, 80)
    b = Fraction(2, 80)
    c = a <= b
    test(True,c) 
    a = Fraction(3, 120)
    b = Fraction(4, 120)
    c = a <= b
    test(True,c) 
    a = Fraction(5, 110)
    b = Fraction(6, 110)
    c = a <= b
    test(True,c) 
    a = Fraction(7, 30)
    b = Fraction(8, 30)
    c = a <= b
    test(True,c) 
    a = Fraction(9, 60)
    b = Fraction(9, 60)
    c = a <= b
    test(True,c) 
    a = Fraction(8, 150)
    b = Fraction(7, 150)
    c = a <= b
    test(False,c) 
    a = Fraction(6, 200)
    b = Fraction(5, 200)
    c = a <= b
    test(False,c) 
    a = Fraction(4, 60)
    b = Fraction(3, 60)
    c = a <= b
    test(False,c) 
    a = Fraction(2, 180)
    b = Fraction(5, 180)
    c = a <= b
    test(True,c) 
    a = Fraction(8, 10)
    b = Fraction(1, 10)
    c = a <= b
    test(False,c) 
    print('testing !=')
    already_printed_error = False
    a = Fraction(1, 180)
    b = Fraction(2, 180)
    c = a != b
    test(True,c) 
    a = Fraction(3, 170)
    b = Fraction(4, 170)
    c = a != b
    test(True,c) 
    a = Fraction(5, 30)
    b = Fraction(6, 30)
    c = a != b
    test(True,c) 
    a = Fraction(7, 120)
    b = Fraction(8, 120)
    c = a != b
    test(True,c) 
    a = Fraction(9, 10)
    b = Fraction(9, 10)
    c = a != b
    test(False,c) 
    a = Fraction(8, 170)
    b = Fraction(7, 170)
    c = a != b
    test(True,c) 
    a = Fraction(6, 130)
    b = Fraction(5, 130)
    c = a != b
    test(True,c) 
    a = Fraction(4, 40)
    b = Fraction(3, 40)
    c = a != b
    test(True,c) 
    a = Fraction(2, 60)
    b = Fraction(5, 60)
    c = a != b
    test(True,c) 
    a = Fraction(8, 20)
    b = Fraction(1, 20)
    c = a != b
    test(True,c) 
    a = Fraction(1, 130)
    b = Fraction(2, 130)
    c = a != b
    test(True,c) 
    a = Fraction(3, 160)
    b = Fraction(4, 160)
    c = a != b
    test(True,c) 
    a = Fraction(5, 100)
    b = Fraction(6, 100)
    c = a != b
    test(True,c) 
    a = Fraction(7, 80)
    b = Fraction(8, 80)
    c = a != b
    test(True,c) 
    a = Fraction(9, 120)
    b = Fraction(9, 120)
    c = a != b
    test(False,c) 
    a = Fraction(8, 40)
    b = Fraction(7, 40)
    c = a != b
    test(True,c) 
    a = Fraction(6, 120)
    b = Fraction(5, 120)
    c = a != b
    test(True,c) 
    a = Fraction(4, 20)
    b = Fraction(3, 20)
    c = a != b
    test(True,c) 
    a = Fraction(2, 140)
    b = Fraction(5, 140)
    c = a != b
    test(True,c) 
    a = Fraction(8, 10)
    b = Fraction(1, 10)
    c = a != b
    test(True,c) 


    print("Ending tests")

test_suite()