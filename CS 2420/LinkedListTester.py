import sys
import time
from LinkedList import LinkedList

already_printed_error = False
def test(expected, given):
    """ Print the result of a test. """
    global already_printed_error
    if already_printed_error == False:
        linenum = sys._getframe(1).f_lineno # Get the caller’s line number.
        if expected == given:
            msg = "Test at line {0} ok.".format(linenum)
            #print(msg)
        else:
            msg = ("\tTest at line {0} FAILED.".format(linenum))
            print(msg)
            print("\t\tExpected: "+ str(expected))
            print("\t\ttype: "+ str(type(expected)))
            print("\t\tGiven   : "+ str(given))
            print("\t\ttype: "+ str(type(given)))
            print("\t\tTester only prints a single error per section - there may be more")
            already_printed_error = True

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    global already_printed_error
    print("Starting tests - only failed tests print unless you change that")
    #Add your tests here

    

    #Dr B's tests follow:
    print('testing __str__')
    already_printed_error = False
    x = LinkedList()
    x.add('periwinkle')
    x.add('abstractedness')
    x.add('meiotic')
    x.add('AAA')
    x.add('Pygmy')
    x.add('Yenisei')
    x.add('Eyck')
    x.add('adulterous')
    test("""[adulterous, Eyck, Yenisei, Pygmy, AAA, meiotic, abstractedness, periwinkle]""", str(x))
    x = LinkedList()
    x.add('hygrometer')
    x.add('Branch')
    x.add('myrmidon')
    x.add('troubleshooting')
    x.add('verify')
    test("""[verify, troubleshooting, myrmidon, Branch, hygrometer]""", str(x))
    x = LinkedList()
    x.add('wearable')
    x.add('Marx')
    x.add('Semitic')
    x.add('Rustbelt')
    x.add('garrulousness')
    test("""[garrulousness, Rustbelt, Semitic, Marx, wearable]""", str(x))
    x = LinkedList()
    x.add('condiment')
    x.add('weedless')
    x.add('Salinas')
    x.add('Florsheim')
    x.add('Kayla')
    x.add('patresfamilias')
    x.add('seduction')
    test("""[seduction, patresfamilias, Kayla, Florsheim, Salinas, weedless, condiment]""", str(x))
    x = LinkedList()
    x.add('Zomba')
    x.add('monocle')
    x.add('correction')
    x.add('Beria')
    test("""[Beria, correction, monocle, Zomba]""", str(x))
    x = LinkedList()
    x.add('irreconcilability')
    x.add('heavily')
    x.add('legislator')
    x.add('gallery')
    x.add('penned')
    test("""[penned, gallery, legislator, heavily, irreconcilability]""", str(x))
    x = LinkedList()
    x.add('laxness')
    x.add('notepaper')
    x.add('hyperspace')
    x.add('quint')
    x.add('lite')
    test("""[lite, quint, hyperspace, notepaper, laxness]""", str(x))
    x = LinkedList()
    x.add('eldest')
    x.add('hailstorm')
    x.add('interface')
    x.add('profitless')
    x.add('competitiveness')
    test("""[competitiveness, profitless, interface, hailstorm, eldest]""", str(x))
    x = LinkedList()
    x.add('chambermaid')
    x.add('seamanship')
    x.add('ibuprofen')
    x.add('Kilroy')
    test("""[Kilroy, ibuprofen, seamanship, chambermaid]""", str(x))
    x = LinkedList()
    x.add('FDR')
    x.add('miraculous')
    x.add('benignity')
    x.add('monopolist')
    x.add('banns')
    test("""[banns, monopolist, benignity, miraculous, FDR]""", str(x))
    x = LinkedList()
    x.add('width')
    x.add('supervene')
    x.add('southeast')
    x.add('distinction')
    x.add('west')
    x.add('exhaustiveness')
    x.add('well')
    test("""[well, exhaustiveness, west, distinction, southeast, supervene, width]""", str(x))
    x = LinkedList()
    x.add('forgetful')
    x.add('execking')
    x.add('roundabout')
    x.add('boundless')
    x.add('architecture')
    x.add('probosces')
    x.add('accessibly')
    test("""[accessibly, probosces, architecture, boundless, roundabout, execking, forgetful]""", str(x))
    x = LinkedList()
    x.add('trust')
    x.add('trillion')
    x.add('thriftiness')
    x.add('crapped')
    x.add('butting')
    x.add('Donna')
    x.add('obituary')
    x.add('workman')
    test("""[workman, obituary, Donna, butting, crapped, thriftiness, trillion, trust]""", str(x))
    x = LinkedList()
    x.add('restructuring')
    x.add('Wonderbra')
    x.add('Finland')
    x.add('Loire')
    x.add('suds')
    test("""[suds, Loire, Finland, Wonderbra, restructuring]""", str(x))
    x = LinkedList()
    x.add('nerd')
    x.add('provolone')
    x.add('illegibly')
    x.add('bunk')
    x.add('soak')
    x.add('brassiness')
    x.add('violin')
    x.add('absolute')
    test("""[absolute, violin, brassiness, soak, bunk, illegibly, provolone, nerd]""", str(x))
    x = LinkedList()
    x.add('Andromache')
    x.add('confirmatory')
    x.add('try')
    x.add('ergo')
    x.add('wiggles')
    x.add('someplace')
    x.add('bifocal')
    x.add('stiffness')
    test("""[stiffness, bifocal, someplace, wiggles, ergo, try, confirmatory, Andromache]""", str(x))
    x = LinkedList()
    x.add('Confederate')
    x.add('Carl')
    x.add('hatband')
    x.add('router')
    x.add('mischief')
    x.add('goober')
    test("""[goober, mischief, router, hatband, Carl, Confederate]""", str(x))
    x = LinkedList()
    x.add('misidentify')
    x.add('goof')
    x.add('stringiness')
    x.add('banish')
    x.add('torturous')
    x.add('Simpson')
    test("""[Simpson, torturous, banish, stringiness, goof, misidentify]""", str(x))
    x = LinkedList()
    x.add('viviparous')
    x.add('teaser')
    x.add('cultist')
    x.add('legato')
    x.add('Rosicrucian')
    test("""[Rosicrucian, legato, cultist, teaser, viviparous]""", str(x))
    x = LinkedList()
    x.add('cyclone')
    x.add('curvature')
    x.add('battlefront')
    x.add('identikit')
    x.add('Ziegler')
    x.add('rho')
    x.add('luckily')
    x.add('Shintoist')
    test("""[Shintoist, luckily, rho, Ziegler, identikit, battlefront, curvature, cyclone]""", str(x))
    print('testing append')
    already_printed_error = False
    x = LinkedList()
    x.append('convectional')
    x.append('antelope')
    x.append('dpi')
    x.append('till')
    x.append('insulting')
    x.append('rugged')
    x.append('bucket')
    x.append('Moroccan')
    test("""[convectional, antelope, dpi, till, insulting, rugged, bucket, Moroccan]""", str(x))
    x = LinkedList()
    x.append('Grus')
    x.append('boundlessness')
    x.append('prismatic')
    x.append('triceratops')
    x.append('pud')
    test("""[Grus, boundlessness, prismatic, triceratops, pud]""", str(x))
    x = LinkedList()
    x.append('fjord')
    x.append('mix')
    x.append('asseveration')
    x.append('twine')
    test("""[fjord, mix, asseveration, twine]""", str(x))
    x = LinkedList()
    x.append('fanlight')
    x.append('bolster')
    x.append('mafia')
    x.append('divergent')
    x.append('Donovan')
    x.append('concordance')
    test("""[fanlight, bolster, mafia, divergent, Donovan, concordance]""", str(x))
    x = LinkedList()
    x.append('disgusting')
    x.append('footling')
    x.append('hallucinatory')
    x.append('backlogging')
    x.append('rapturous')
    test("""[disgusting, footling, hallucinatory, backlogging, rapturous]""", str(x))
    x = LinkedList()
    x.append('Charity')
    x.append('wires')
    x.append('psephology')
    x.append('hep')
    x.append('rutted')
    test("""[Charity, wires, psephology, hep, rutted]""", str(x))
    x = LinkedList()
    x.append('highboy')
    x.append('qt')
    x.append('Vlasic')
    x.append('iron')
    x.append('Weissmuller')
    x.append('knight')
    x.append('Ramada')
    x.append('experimentation')
    test("""[highboy, qt, Vlasic, iron, Weissmuller, knight, Ramada, experimentation]""", str(x))
    x = LinkedList()
    x.append('weedkiller')
    x.append('amiably')
    x.append('negotiator')
    x.append('pulchritudinous')
    test("""[weedkiller, amiably, negotiator, pulchritudinous]""", str(x))
    x = LinkedList()
    x.append('toga')
    x.append('niggard')
    x.append('ado')
    x.append('twin')
    test("""[toga, niggard, ado, twin]""", str(x))
    x = LinkedList()
    x.append('archbishop')
    x.append('twinkling')
    x.append('docudrama')
    x.append('Emanuel')
    x.append('Florida')
    test("""[archbishop, twinkling, docudrama, Emanuel, Florida]""", str(x))
    x = LinkedList()
    x.append('blubber')
    x.append('cashier')
    x.append('outwitting')
    x.append('Gross')
    x.append('nonsurgical')
    x.append('minuteness')
    x.append('Scythian')
    test("""[blubber, cashier, outwitting, Gross, nonsurgical, minuteness, Scythian]""", str(x))
    x = LinkedList()
    x.append('berm')
    x.append('principle')
    x.append('whirl')
    x.append('plenum')
    x.append('characterization')
    x.append('roil')
    test("""[berm, principle, whirl, plenum, characterization, roil]""", str(x))
    x = LinkedList()
    x.append('abyss')
    x.append('hypermarket')
    x.append('thirteenth')
    x.append('scrawl')
    x.append('heir')
    test("""[abyss, hypermarket, thirteenth, scrawl, heir]""", str(x))
    x = LinkedList()
    x.append('Beirut')
    x.append('isotopic')
    x.append('freeman')
    x.append('underwhelm')
    x.append('lucky')
    x.append('cursoriness')
    x.append('surliness')
    x.append('tinkle')
    test("""[Beirut, isotopic, freeman, underwhelm, lucky, cursoriness, surliness, tinkle]""", str(x))
    x = LinkedList()
    x.append('lock')
    x.append('armhole')
    x.append('wrangle')
    x.append('cumbersomeness')
    x.append('Corinthians')
    x.append('impassibility')
    test("""[lock, armhole, wrangle, cumbersomeness, Corinthians, impassibility]""", str(x))
    x = LinkedList()
    x.append('tutor')
    x.append('Goering')
    x.append('Shasta')
    x.append('Arneb')
    x.append('guise')
    x.append('bustle')
    x.append('blown')
    test("""[tutor, Goering, Shasta, Arneb, guise, bustle, blown]""", str(x))
    x = LinkedList()
    x.append('fermented')
    x.append('slavery')
    x.append('Banting')
    x.append('reteach')
    x.append('elongation')
    test("""[fermented, slavery, Banting, reteach, elongation]""", str(x))
    x = LinkedList()
    x.append('help')
    x.append('libation')
    x.append('endeavor')
    x.append('incomplete')
    x.append('plateful')
    x.append('topflight')
    x.append('cottager')
    x.append('Isuzu')
    test("""[help, libation, endeavor, incomplete, plateful, topflight, cottager, Isuzu]""", str(x))
    x = LinkedList()
    x.append('Indore')
    x.append('punctual')
    x.append('stickler')
    x.append('brickyard')
    x.append('incorporate')
    test("""[Indore, punctual, stickler, brickyard, incorporate]""", str(x))
    x = LinkedList()
    x.append('Houston')
    x.append('megabyte')
    x.append('housekeeper')
    x.append('scruffiness')
    x.append('protectionism')
    test("""[Houston, megabyte, housekeeper, scruffiness, protectionism]""", str(x))
    print('testing index')
    already_printed_error = False
    x = LinkedList()
    x.add('racialism')
    x.add('stride')
    x.add('bran')
    x.add('amass')
    x.add('Platonism')
    x.add('keynoter')
    x.add('ibex')
    x.add('anticked')
    test(3, x.index('Platonism'))
    test(5, x.index('bran'))
    test(2, x.index('keynoter'))
    test(1, x.index('ibex'))
    test(7, x.index('racialism'))
    test(0, x.index('anticked'))
    test(6, x.index('stride'))
    test(4, x.index('amass'))
    try:
        x.index('Oort')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('polytechnic')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('weekend')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Rickey')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('gladder')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Marlon')
    x.add('abject')
    x.add('meadow')
    x.add('SE')
    x.add('professorial')
    test(1, x.index('SE'))
    test(2, x.index('meadow'))
    test(3, x.index('abject'))
    test(4, x.index('Marlon'))
    test(0, x.index('professorial'))
    try:
        x.index('embower')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('borrower')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('croissant')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('originality')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('criticizer')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('mosque')
    x.add('playacting')
    x.add('etching')
    x.add('flunk')
    x.add('farcical')
    x.add('moonwalk')
    x.add('siesta')
    x.add('pellucid')
    test(0, x.index('pellucid'))
    test(1, x.index('siesta'))
    test(4, x.index('flunk'))
    test(5, x.index('etching'))
    test(2, x.index('moonwalk'))
    test(7, x.index('mosque'))
    test(3, x.index('farcical'))
    test(6, x.index('playacting'))
    try:
        x.index('Inge')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('impetuousness')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('resuscitator')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Farrell')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Risorgimento')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('dreamlike')
    x.add('recurrence')
    x.add('Pen')
    x.add('statehouse')
    x.add('wellness')
    test(2, x.index('Pen'))
    test(3, x.index('recurrence'))
    test(1, x.index('statehouse'))
    test(4, x.index('dreamlike'))
    test(0, x.index('wellness'))
    try:
        x.index('samurai')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('FORTRAN')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('clementine')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('utilization')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('riverfront')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('genteel')
    x.add('effluence')
    x.add('cobra')
    x.add('teamwork')
    x.add('Craig')
    x.add('Jerald')
    x.add('Djibouti')
    x.add('padlock')
    test(3, x.index('Craig'))
    test(6, x.index('effluence'))
    test(2, x.index('Jerald'))
    test(4, x.index('teamwork'))
    test(0, x.index('padlock'))
    test(7, x.index('genteel'))
    test(1, x.index('Djibouti'))
    test(5, x.index('cobra'))
    try:
        x.index('cementum')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('kissogram')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('leaper')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('parsec')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Norfolk')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('enunciation')
    x.add('calabash')
    x.add('definitions')
    x.add('bootless')
    test(1, x.index('definitions'))
    test(0, x.index('bootless'))
    test(2, x.index('calabash'))
    test(3, x.index('enunciation'))
    try:
        x.index('rubbernecker')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Helvetius')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('HI')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Zion')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('inimitably')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Parcheesi')
    x.add('oversell')
    x.add('Tammany')
    x.add('buckle')
    x.add('presbytery')
    x.add('shant')
    x.add('ideograph')
    x.add('marmalade')
    test(5, x.index('Tammany'))
    test(4, x.index('buckle'))
    test(1, x.index('ideograph'))
    test(6, x.index('oversell'))
    test(7, x.index('Parcheesi'))
    test(0, x.index('marmalade'))
    test(3, x.index('presbytery'))
    test(2, x.index('shant'))
    try:
        x.index('glibness')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('nudity')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('cuss')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('interchange')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('stocky')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('pictograph')
    x.add('synthesis')
    x.add('reasoning')
    x.add('phosphate')
    x.add('deduct')
    x.add('Alberio')
    test(0, x.index('Alberio'))
    test(2, x.index('phosphate'))
    test(1, x.index('deduct'))
    test(3, x.index('reasoning'))
    test(5, x.index('pictograph'))
    test(4, x.index('synthesis'))
    try:
        x.index('moistener')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('bookcase')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('manipulable')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('bootstrapped')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Polaroid')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('emergence')
    x.add('yall')
    x.add('emceeing')
    x.add('require')
    x.add('musclebound')
    x.add('TA')
    test(5, x.index('emergence'))
    test(0, x.index('TA'))
    test(3, x.index('emceeing'))
    test(1, x.index('musclebound'))
    test(4, x.index('yall'))
    test(2, x.index('require'))
    try:
        x.index('craftswomen')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Gardner')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('kale')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('wiener')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('burliness')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('monition')
    x.add('conditions')
    x.add('phonic')
    x.add('timpani')
    x.add('sailcloth')
    x.add('pressing')
    test(0, x.index('pressing'))
    test(4, x.index('conditions'))
    test(2, x.index('timpani'))
    test(3, x.index('phonic'))
    test(1, x.index('sailcloth'))
    test(5, x.index('monition'))
    try:
        x.index('hireling')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('bullfinch')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('temple')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('astrophysicist')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('pacer')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('contradict')
    x.add('radiant')
    x.add('wirehair')
    x.add('Cognac')
    x.add('Pabst')
    test(2, x.index('wirehair'))
    test(3, x.index('radiant'))
    test(4, x.index('contradict'))
    test(0, x.index('Pabst'))
    test(1, x.index('Cognac'))
    try:
        x.index('backroom')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('eccentric')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('pertussis')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('melange')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('scrammed')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('archdeacon')
    x.add('Thespis')
    x.add('sightly')
    x.add('tissue')
    x.add('parkland')
    x.add('regexp')
    test(0, x.index('regexp'))
    test(4, x.index('Thespis'))
    test(2, x.index('tissue'))
    test(1, x.index('parkland'))
    test(3, x.index('sightly'))
    test(5, x.index('archdeacon'))
    try:
        x.index('paracetamol')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('psst')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('upsetting')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('zygotic')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('halting')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('multiplicative')
    x.add('snapdragon')
    x.add('honorific')
    x.add('obverse')
    test(0, x.index('obverse'))
    test(1, x.index('honorific'))
    test(3, x.index('multiplicative'))
    test(2, x.index('snapdragon'))
    try:
        x.index('Orly')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Wezen')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('gunning')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('resiliency')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('patrolled')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('rebidding')
    x.add('testamentary')
    x.add('irrupt')
    x.add('flambeed')
    test(1, x.index('irrupt'))
    test(2, x.index('testamentary'))
    test(0, x.index('flambeed'))
    test(3, x.index('rebidding'))
    try:
        x.index('fibbing')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('sty')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('microbiologist')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('thievish')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('tubful')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('shaft')
    x.add('atop')
    x.add('turbojet')
    x.add('Lodge')
    test(3, x.index('shaft'))
    test(0, x.index('Lodge'))
    test(2, x.index('atop'))
    test(1, x.index('turbojet'))
    try:
        x.index('jean')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('hesitating')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('syncopation')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Chihuahua')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('trimmed')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Toronto')
    x.add('sex')
    x.add('necklace')
    x.add('tribunal')
    x.add('intrastate')
    x.add('ravishing')
    x.add('uppish')
    test(0, x.index('uppish'))
    test(6, x.index('Toronto'))
    test(4, x.index('necklace'))
    test(3, x.index('tribunal'))
    test(1, x.index('ravishing'))
    test(5, x.index('sex'))
    test(2, x.index('intrastate'))
    try:
        x.index('LED')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('businesslike')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('extrajudicial')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('symbol')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('finder')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Khorana')
    x.add('unfailing')
    x.add('porringer')
    x.add('computing')
    x.add('residuum')
    x.add('bushing')
    x.add('separability')
    x.add('hypocritical')
    test(1, x.index('separability'))
    test(3, x.index('residuum'))
    test(4, x.index('computing'))
    test(7, x.index('Khorana'))
    test(0, x.index('hypocritical'))
    test(5, x.index('porringer'))
    test(6, x.index('unfailing'))
    test(2, x.index('bushing'))
    try:
        x.index('dielectric')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('romeo')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('steering')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('quadrennial')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('unwieldiness')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('prowl')
    x.add('Rwanda')
    x.add('cruft')
    x.add('bizarre')
    x.add('dementia')
    x.add('Photostatting')
    x.add('seedy')
    x.add('dependably')
    test(1, x.index('seedy'))
    test(0, x.index('dependably'))
    test(4, x.index('bizarre'))
    test(2, x.index('Photostatting'))
    test(3, x.index('dementia'))
    test(7, x.index('prowl'))
    test(5, x.index('cruft'))
    test(6, x.index('Rwanda'))
    try:
        x.index('cornet')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('constitutionalism')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('sawhorse')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('immature')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('offensives')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Ricky')
    x.add('meteoroid')
    x.add('Rio')
    x.add('Rasmussen')
    x.add('wheat')
    x.add('lignite')
    test(5, x.index('Ricky'))
    test(3, x.index('Rio'))
    test(4, x.index('meteoroid'))
    test(0, x.index('lignite'))
    test(1, x.index('wheat'))
    test(2, x.index('Rasmussen'))
    try:
        x.index('submergence')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('enzymatic')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('ureter')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('myopically')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('drake')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('fluxing')
    x.add('humanism')
    x.add('mummification')
    x.add('Brianna')
    x.add('BBSes')
    x.add('partake')
    test(4, x.index('humanism'))
    test(0, x.index('partake'))
    test(3, x.index('mummification'))
    test(1, x.index('BBSes'))
    test(5, x.index('fluxing'))
    test(2, x.index('Brianna'))
    try:
        x.index('thieve')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Floyd')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('relinquish')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('thinnest')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('grandeur')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    print('testing insert')
    already_printed_error = False
    x = LinkedList()
    x.insert(0, 'buzzer')
    x.insert(0, 'Aristarchus')
    x.insert(0, 'Ian')
    x.insert(2, 'abreast')
    x.insert(0, 'produces')
    test(0, x.index('produces'))
    test(2, x.index('Aristarchus'))
    test(1, x.index('Ian'))
    test(4, x.index('buzzer'))
    test(3, x.index('abreast'))
    try:
        x.index('guilder')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('plow')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Singapore')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Dame')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('ninepin')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'Donnie')
    x.insert(0, 'deafness')
    x.insert(1, 'Kirghistan')
    x.insert(2, 'spavin')
    x.insert(1, 'heartsick')
    x.insert(2, 'slid')
    x.insert(1, 'lightness')
    x.insert(0, 'baptizer')
    test(2, x.index('lightness'))
    test(3, x.index('heartsick'))
    test(0, x.index('baptizer'))
    test(1, x.index('deafness'))
    test(4, x.index('slid'))
    test(7, x.index('Donnie'))
    test(6, x.index('spavin'))
    test(5, x.index('Kirghistan'))
    try:
        x.index('crunchy')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('unfeminine')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('argon')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('gridiron')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('destructibility')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'core')
    x.insert(0, 'bodybuilder')
    x.insert(0, 'misinformation')
    x.insert(1, 'theocratic')
    x.insert(2, 'bomb')
    x.insert(4, 'ungentle')
    test(0, x.index('misinformation'))
    test(3, x.index('bodybuilder'))
    test(5, x.index('core'))
    test(2, x.index('bomb'))
    test(4, x.index('ungentle'))
    test(1, x.index('theocratic'))
    try:
        x.index('rumbling')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Meagan')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('overrun')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('pg')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('thousandths')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'Donetsk')
    x.insert(0, 'Ashmolean')
    x.insert(0, 't')
    x.insert(1, 'uprising')
    test(1, x.index('uprising'))
    test(2, x.index('Ashmolean'))
    test(3, x.index('Donetsk'))
    test(0, x.index('t'))
    try:
        x.index('mound')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Visayans')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('slapper')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('stationer')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Stout')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'microeconomics')
    x.insert(0, 'Thomas')
    x.insert(1, 'lyncher')
    x.insert(2, 'crosstown')
    x.insert(3, 'coin')
    x.insert(1, 'VHF')
    x.insert(2, 'alter')
    test(0, x.index('Thomas'))
    test(1, x.index('VHF'))
    test(6, x.index('microeconomics'))
    test(2, x.index('alter'))
    test(4, x.index('crosstown'))
    test(3, x.index('lyncher'))
    test(5, x.index('coin'))
    try:
        x.index('covert')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('vocational')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('suffuse')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('consortia')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('washtub')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'tiger')
    x.insert(0, 'markkaa')
    x.insert(1, 'meadowlark')
    x.insert(0, 'Tiberius')
    x.insert(3, 'forbade')
    x.insert(3, 'magnificence')
    x.insert(5, 'windflower')
    test(4, x.index('forbade'))
    test(1, x.index('markkaa'))
    test(6, x.index('tiger'))
    test(0, x.index('Tiberius'))
    test(3, x.index('magnificence'))
    test(2, x.index('meadowlark'))
    test(5, x.index('windflower'))
    try:
        x.index('sabot')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('schoolchildren')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('caramelize')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Uniroyal')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('deluge')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'immanent')
    x.insert(0, 'exasperated')
    x.insert(1, 'emigrate')
    x.insert(2, 'gulp')
    x.insert(0, 'Scientology')
    x.insert(1, 'heroes')
    x.insert(0, 'journalism')
    x.insert(3, 'politico')
    test(2, x.index('heroes'))
    test(7, x.index('immanent'))
    test(5, x.index('emigrate'))
    test(6, x.index('gulp'))
    test(3, x.index('politico'))
    test(1, x.index('Scientology'))
    test(4, x.index('exasperated'))
    test(0, x.index('journalism'))
    try:
        x.index('counterpoise')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('cystic')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('craftspeople')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('dissuade')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('stubble')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'asceticism')
    x.insert(0, 'daemon')
    x.insert(1, 'perplex')
    x.insert(0, 'overpaid')
    test(3, x.index('asceticism'))
    test(2, x.index('perplex'))
    test(1, x.index('daemon'))
    test(0, x.index('overpaid'))
    try:
        x.index('electrocute')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('penal')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('croaky')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('driver')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Surinamese')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'pleb')
    x.insert(0, 'nonsympathizer')
    x.insert(0, 'artist')
    x.insert(1, 'striation')
    x.insert(1, 'Leonardo')
    x.insert(1, 'brainwave')
    x.insert(4, 'Cincinnati')
    x.insert(1, 'unmissable')
    test(0, x.index('artist'))
    test(1, x.index('unmissable'))
    test(7, x.index('pleb'))
    test(2, x.index('brainwave'))
    test(3, x.index('Leonardo'))
    test(5, x.index('Cincinnati'))
    test(6, x.index('nonsympathizer'))
    test(4, x.index('striation'))
    try:
        x.index('inefficiency')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('dependable')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('future')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Kutuzov')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('gizzard')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'Therese')
    x.insert(0, 'sisterhood')
    x.insert(0, 'vegetarian')
    x.insert(2, 'accusatory')
    x.insert(1, 'siliceous')
    x.insert(1, 'caliphate')
    x.insert(1, 'Tainan')
    test(0, x.index('vegetarian'))
    test(3, x.index('siliceous'))
    test(1, x.index('Tainan'))
    test(6, x.index('Therese'))
    test(2, x.index('caliphate'))
    test(4, x.index('sisterhood'))
    test(5, x.index('accusatory'))
    try:
        x.index('misinform')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('thulium')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Muhammadan')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Uccello')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('boulevard')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'stoop')
    x.insert(0, 'grisliness')
    x.insert(1, 'Panamanian')
    x.insert(2, 'Italy')
    x.insert(3, 'LG')
    x.insert(0, 'stagger')
    x.insert(2, 'nightwear')
    x.insert(1, 'rottweiler')
    test(2, x.index('grisliness'))
    test(5, x.index('Italy'))
    test(1, x.index('rottweiler'))
    test(3, x.index('nightwear'))
    test(6, x.index('LG'))
    test(7, x.index('stoop'))
    test(4, x.index('Panamanian'))
    test(0, x.index('stagger'))
    try:
        x.index('exception')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Scriabin')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Audra')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Pfizer')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('backbreaking')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'sideline')
    x.insert(0, 'hotshot')
    x.insert(0, 'Gaul')
    x.insert(2, 'twee')
    x.insert(0, 'homeostatic')
    x.insert(2, 'citrus')
    x.insert(2, 'vicarious')
    x.insert(5, 'pretax')
    test(5, x.index('pretax'))
    test(1, x.index('Gaul'))
    test(2, x.index('vicarious'))
    test(4, x.index('hotshot'))
    test(6, x.index('twee'))
    test(3, x.index('citrus'))
    test(7, x.index('sideline'))
    test(0, x.index('homeostatic'))
    try:
        x.index('accessory')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('collard')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('gnaw')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Capetian')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('different')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'auricular')
    x.insert(0, 'Irene')
    x.insert(0, 'flamethrower')
    x.insert(0, 'reckon')
    x.insert(0, 'nonrefillable')
    test(1, x.index('reckon'))
    test(0, x.index('nonrefillable'))
    test(3, x.index('Irene'))
    test(2, x.index('flamethrower'))
    test(4, x.index('auricular'))
    try:
        x.index('diabolic')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('belly')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('coll')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('dressmaking')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Rd')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'trinity')
    x.insert(0, 'lusciousness')
    x.insert(0, 'Balearic')
    x.insert(2, 'informant')
    x.insert(2, 'monomaniacal')
    x.insert(0, 'cornflour')
    x.insert(0, 'incandescence')
    x.insert(6, 'suckling')
    test(5, x.index('informant'))
    test(6, x.index('suckling'))
    test(0, x.index('incandescence'))
    test(1, x.index('cornflour'))
    test(4, x.index('monomaniacal'))
    test(2, x.index('Balearic'))
    test(3, x.index('lusciousness'))
    test(7, x.index('trinity'))
    try:
        x.index('infamy')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('elocution')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('hardwired')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('vascular')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Octavio')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'committing')
    x.insert(0, 'esoterically')
    x.insert(1, 'interactive')
    x.insert(2, 'silliness')
    x.insert(0, 'publican')
    x.insert(0, 'airdropped')
    test(2, x.index('esoterically'))
    test(0, x.index('airdropped'))
    test(3, x.index('interactive'))
    test(4, x.index('silliness'))
    test(5, x.index('committing'))
    test(1, x.index('publican'))
    try:
        x.index('luxuriant')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('cw')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('malignant')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Bayesian')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('embarrassed')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'sapper')
    x.insert(0, 'Cecile')
    x.insert(0, 'acrobat')
    x.insert(0, 'Balzac')
    x.insert(0, 'screenshot')
    x.insert(1, 'spectator')
    x.insert(1, 'lingoes')
    x.insert(0, 'infinitesimal')
    test(3, x.index('spectator'))
    test(5, x.index('acrobat'))
    test(7, x.index('sapper'))
    test(0, x.index('infinitesimal'))
    test(4, x.index('Balzac'))
    test(6, x.index('Cecile'))
    test(1, x.index('screenshot'))
    test(2, x.index('lingoes'))
    try:
        x.index('homogenization')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('introduction')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('yukky')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Mallory')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('oi')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'Scythia')
    x.insert(0, 'maw')
    x.insert(1, 'beseem')
    x.insert(2, 'depth')
    x.insert(0, 'misplace')
    x.insert(2, 'Roxanne')
    x.insert(1, 'protectionist')
    x.insert(1, 'blancmange')
    test(5, x.index('beseem'))
    test(3, x.index('maw'))
    test(1, x.index('blancmange'))
    test(6, x.index('depth'))
    test(2, x.index('protectionist'))
    test(7, x.index('Scythia'))
    test(4, x.index('Roxanne'))
    test(0, x.index('misplace'))
    try:
        x.index('daub')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('scrofula')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('singleton')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('buttermilk')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('loos')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'powerlessness')
    x.insert(0, 'autograph')
    x.insert(1, 'frigid')
    x.insert(1, 'Aymara')
    x.insert(0, 'anticipated')
    x.insert(2, 'favorable')
    x.insert(5, 'expelled')
    test(2, x.index('favorable'))
    test(6, x.index('powerlessness'))
    test(4, x.index('frigid'))
    test(5, x.index('expelled'))
    test(3, x.index('Aymara'))
    test(0, x.index('anticipated'))
    test(1, x.index('autograph'))
    try:
        x.index('imperialist')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('compo')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Marduk')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('archer')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('scale')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'McClure')
    x.insert(0, 'embarrassing')
    x.insert(0, 'Rather')
    x.insert(2, 'forefather')
    x.insert(1, 'Sherrie')
    x.insert(4, 'Doctorow')
    x.insert(2, 'rawness')
    test(6, x.index('McClure'))
    test(1, x.index('Sherrie'))
    test(2, x.index('rawness'))
    test(5, x.index('Doctorow'))
    test(3, x.index('embarrassing'))
    test(4, x.index('forefather'))
    test(0, x.index('Rather'))
    try:
        x.index('stammering')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('upstroke')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('American')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('lithosphere')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('attentions')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.insert(0, 'helpmate')
    x.insert(0, 'blagged')
    x.insert(1, 'atavistic')
    x.insert(1, 'curiosity')
    x.insert(1, 'Aaliyah')
    test(2, x.index('curiosity'))
    test(4, x.index('helpmate'))
    test(3, x.index('atavistic'))
    test(1, x.index('Aaliyah'))
    test(0, x.index('blagged'))
    try:
        x.index('muenster')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('malathion')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('Buffy')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('missus')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    try:
        x.index('pragmatist')
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    print('testing pop')
    already_printed_error = False
    x = LinkedList()
    x.add('Jaclyn')
    x.add('vagary')
    x.add('jurymen')
    x.add('microcircuit')
    test('Jaclyn', x.pop())
    test('vagary', x.pop())
    test('jurymen', x.pop())
    test('microcircuit', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('curvy')
    x.add('intercollegiate')
    x.add('tomboyish')
    x.add('soporifically')
    test('curvy', x.pop())
    test('intercollegiate', x.pop())
    test('tomboyish', x.pop())
    test('soporifically', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Neapolitan')
    x.add('snuggle')
    x.add('homage')
    x.add('guiltiness')
    x.add('revenuer')
    x.add('dipped')
    x.add('inductance')
    test('Neapolitan', x.pop())
    test('snuggle', x.pop())
    test('homage', x.pop())
    test('guiltiness', x.pop())
    test('revenuer', x.pop())
    test('dipped', x.pop())
    test('inductance', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Waring')
    x.add('bathroom')
    x.add('betoken')
    x.add('Weierstrass')
    test('Waring', x.pop())
    test('bathroom', x.pop())
    test('betoken', x.pop())
    test('Weierstrass', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('immodest')
    x.add('Willamette')
    x.add('Demavend')
    x.add('wormy')
    test('immodest', x.pop())
    test('Willamette', x.pop())
    test('Demavend', x.pop())
    test('wormy', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('initiator')
    x.add('obsessive')
    x.add('ripcord')
    x.add('whatchamacallit')
    x.add('workingwoman')
    x.add('counterpane')
    x.add('Yaroslavl')
    x.add('shed')
    test('initiator', x.pop())
    test('obsessive', x.pop())
    test('ripcord', x.pop())
    test('whatchamacallit', x.pop())
    test('workingwoman', x.pop())
    test('counterpane', x.pop())
    test('Yaroslavl', x.pop())
    test('shed', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('lethargically')
    x.add('wick')
    x.add('abbreviate')
    x.add('forget')
    x.add('breech')
    test('lethargically', x.pop())
    test('wick', x.pop())
    test('abbreviate', x.pop())
    test('forget', x.pop())
    test('breech', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('vapor')
    x.add('meatiness')
    x.add('apprehensiveness')
    x.add('jolliness')
    x.add('winsomeness')
    test('vapor', x.pop())
    test('meatiness', x.pop())
    test('apprehensiveness', x.pop())
    test('jolliness', x.pop())
    test('winsomeness', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Hangul')
    x.add('ending')
    x.add('Poirot')
    x.add('arboretum')
    x.add('seventieths')
    x.add('inhumane')
    test('Hangul', x.pop())
    test('ending', x.pop())
    test('Poirot', x.pop())
    test('arboretum', x.pop())
    test('seventieths', x.pop())
    test('inhumane', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('taxer')
    x.add('breadbasket')
    x.add('quit')
    x.add('chapati')
    x.add('placer')
    x.add('coolant')
    test('taxer', x.pop())
    test('breadbasket', x.pop())
    test('quit', x.pop())
    test('chapati', x.pop())
    test('placer', x.pop())
    test('coolant', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('yapped')
    x.add('Minuit')
    x.add('Dianna')
    x.add('gone')
    x.add('ugliness')
    x.add('client')
    x.add('vary')
    test('yapped', x.pop())
    test('Minuit', x.pop())
    test('Dianna', x.pop())
    test('gone', x.pop())
    test('ugliness', x.pop())
    test('client', x.pop())
    test('vary', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('unicycle')
    x.add('orientations')
    x.add('bacteria')
    x.add('contextualize')
    test('unicycle', x.pop())
    test('orientations', x.pop())
    test('bacteria', x.pop())
    test('contextualize', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Monica')
    x.add('brambly')
    x.add('Houdini')
    x.add('libertarian')
    x.add('roger')
    x.add('stratum')
    test('Monica', x.pop())
    test('brambly', x.pop())
    test('Houdini', x.pop())
    test('libertarian', x.pop())
    test('roger', x.pop())
    test('stratum', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('sorrowful')
    x.add('Gillespie')
    x.add('Venice')
    x.add('tatted')
    x.add('batty')
    test('sorrowful', x.pop())
    test('Gillespie', x.pop())
    test('Venice', x.pop())
    test('tatted', x.pop())
    test('batty', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('explain')
    x.add('orchestral')
    x.add('horologic')
    x.add('minority')
    x.add('ham')
    x.add('bountiful')
    test('explain', x.pop())
    test('orchestral', x.pop())
    test('horologic', x.pop())
    test('minority', x.pop())
    test('ham', x.pop())
    test('bountiful', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Aeneid')
    x.add('JPEG')
    x.add('drat')
    x.add('fulmination')
    x.add('crud')
    x.add('Peters')
    x.add('chronically')
    x.add('Carla')
    test('Aeneid', x.pop())
    test('JPEG', x.pop())
    test('drat', x.pop())
    test('fulmination', x.pop())
    test('crud', x.pop())
    test('Peters', x.pop())
    test('chronically', x.pop())
    test('Carla', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('constitutionality')
    x.add('lend')
    x.add('stampede')
    x.add('howitzer')
    x.add('why')
    x.add('highness')
    test('constitutionality', x.pop())
    test('lend', x.pop())
    test('stampede', x.pop())
    test('howitzer', x.pop())
    test('why', x.pop())
    test('highness', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('tool')
    x.add('ilium')
    x.add('fluoridate')
    x.add('solidification')
    x.add('Phillipa')
    x.add('biog')
    test('tool', x.pop())
    test('ilium', x.pop())
    test('fluoridate', x.pop())
    test('solidification', x.pop())
    test('Phillipa', x.pop())
    test('biog', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('smash')
    x.add('plugin')
    x.add('phoniness')
    x.add('trapped')
    x.add('suggestibility')
    x.add('ejaculation')
    x.add('womb')
    x.add('inclination')
    test('smash', x.pop())
    test('plugin', x.pop())
    test('phoniness', x.pop())
    test('trapped', x.pop())
    test('suggestibility', x.pop())
    test('ejaculation', x.pop())
    test('womb', x.pop())
    test('inclination', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('utter')
    x.add('solidness')
    x.add('waste')
    x.add('mineralogical')
    x.add('frugal')
    x.add('wolfhound')
    x.add('Dubai')
    x.add('Minnesota')
    test('utter', x.pop())
    test('solidness', x.pop())
    test('waste', x.pop())
    test('mineralogical', x.pop())
    test('frugal', x.pop())
    test('wolfhound', x.pop())
    test('Dubai', x.pop())
    test('Minnesota', x.pop())
    try:
        x.pop()
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    print('testing pop_at_position')
    already_printed_error = False
    x = LinkedList()
    x.add('motocross')
    x.add('smirch')
    x.add('malicious')
    x.add('execution')
    x.add('decibel')
    test('smirch', x.pop_at_position(3))
    try:
        x.pop_at_position(8)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('execution', x.pop_at_position(1))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('malicious', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('motocross', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('decibel', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('parking')
    x.add('rightist')
    x.add('Fitzpatrick')
    x.add('gymnast')
    test('Fitzpatrick', x.pop_at_position(1))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('gymnast', x.pop_at_position(0))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('parking', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('rightist', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('sorcerer')
    x.add('heartless')
    x.add('goddamn')
    x.add('highway')
    x.add('heave')
    x.add('skipping')
    x.add('snort')
    test('skipping', x.pop_at_position(1))
    try:
        x.pop_at_position(8)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('heave', x.pop_at_position(1))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('heartless', x.pop_at_position(3))
    try:
        x.pop_at_position(8)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('sorcerer', x.pop_at_position(3))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('goddamn', x.pop_at_position(2))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('highway', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('snort', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Louisianian')
    x.add('organization')
    x.add('Rose')
    x.add('accuser')
    x.add('Mekong')
    test('Rose', x.pop_at_position(2))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('organization', x.pop_at_position(2))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('accuser', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Louisianian', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Mekong', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('unicorn')
    x.add('Usenet')
    x.add('measurement')
    x.add('popgun')
    x.add('cheer')
    x.add('fitly')
    test('Usenet', x.pop_at_position(4))
    try:
        x.pop_at_position(10)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('fitly', x.pop_at_position(0))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('cheer', x.pop_at_position(0))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('measurement', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('unicorn', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('popgun', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('portraitist')
    x.add('inscrutableness')
    x.add('inhabited')
    x.add('doorknocker')
    x.add('grinning')
    test('portraitist', x.pop_at_position(4))
    try:
        x.pop_at_position(9)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('doorknocker', x.pop_at_position(1))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('grinning', x.pop_at_position(0))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('inscrutableness', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('inhabited', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('folksiness')
    x.add('Hindustani')
    x.add('moggy')
    x.add('philatelic')
    x.add('hasp')
    x.add('petrologist')
    test('philatelic', x.pop_at_position(2))
    try:
        x.pop_at_position(8)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('hasp', x.pop_at_position(1))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('folksiness', x.pop_at_position(3))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('moggy', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('petrologist', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Hindustani', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('overestimate')
    x.add('stateswoman')
    x.add('comfy')
    x.add('roman')
    x.add('glen')
    x.add('honester')
    x.add('someone')
    x.add('Delmar')
    test('overestimate', x.pop_at_position(7))
    try:
        x.pop_at_position(15)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('stateswoman', x.pop_at_position(6))
    try:
        x.pop_at_position(13)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('glen', x.pop_at_position(3))
    try:
        x.pop_at_position(9)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('comfy', x.pop_at_position(4))
    try:
        x.pop_at_position(9)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('roman', x.pop_at_position(3))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('someone', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('honester', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Delmar', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('menacing')
    x.add('Namibia')
    x.add('Hazlitt')
    x.add('bang')
    x.add('flatted')
    x.add('Minerva')
    x.add('bestrewn')
    x.add('billboard')
    test('Hazlitt', x.pop_at_position(5))
    try:
        x.pop_at_position(13)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Namibia', x.pop_at_position(5))
    try:
        x.pop_at_position(12)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('menacing', x.pop_at_position(5))
    try:
        x.pop_at_position(11)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Minerva', x.pop_at_position(2))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('billboard', x.pop_at_position(0))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('bang', x.pop_at_position(2))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('bestrewn', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('flatted', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('insurrection')
    x.add('compulsory')
    x.add('cantabile')
    x.add('Gehrig')
    x.add('circularity')
    x.add('breast')
    x.add('morphing')
    test('circularity', x.pop_at_position(2))
    try:
        x.pop_at_position(9)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('breast', x.pop_at_position(1))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('insurrection', x.pop_at_position(4))
    try:
        x.pop_at_position(9)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Gehrig', x.pop_at_position(1))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('cantabile', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('morphing', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('compulsory', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('each')
    x.add('om')
    x.add('painkilling')
    x.add('farther')
    x.add('muffle')
    x.add('sarky')
    x.add('blacktopped')
    test('each', x.pop_at_position(6))
    try:
        x.pop_at_position(13)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('sarky', x.pop_at_position(1))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('painkilling', x.pop_at_position(3))
    try:
        x.pop_at_position(8)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('blacktopped', x.pop_at_position(0))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('om', x.pop_at_position(2))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('muffle', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('farther', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('Puck')
    x.add('gyrator')
    x.add('semiofficial')
    x.add('startling')
    x.add('geomagnetic')
    x.add('indissolubility')
    test('startling', x.pop_at_position(2))
    try:
        x.pop_at_position(8)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('geomagnetic', x.pop_at_position(1))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('indissolubility', x.pop_at_position(0))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('gyrator', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Puck', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('semiofficial', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('plasterboard')
    x.add('nightcap')
    x.add('firth')
    x.add('harasser')
    test('nightcap', x.pop_at_position(2))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('firth', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('harasser', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('plasterboard', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('perfectibility')
    x.add('lxii')
    x.add('evangelic')
    x.add('guestroom')
    x.add('bun')
    x.add('ageism')
    x.add('monarchical')
    test('evangelic', x.pop_at_position(4))
    try:
        x.pop_at_position(11)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('lxii', x.pop_at_position(4))
    try:
        x.pop_at_position(10)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('ageism', x.pop_at_position(1))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('perfectibility', x.pop_at_position(3))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('monarchical', x.pop_at_position(0))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('bun', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('guestroom', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('function')
    x.add('fitter')
    x.add('infestation')
    x.add('phat')
    test('function', x.pop_at_position(3))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('phat', x.pop_at_position(0))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('infestation', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('fitter', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('decor')
    x.add('appellate')
    x.add('Sunbelt')
    x.add('hetero')
    x.add('Isabel')
    x.add('khan')
    x.add('NDjamena')
    x.add('polymer')
    test('appellate', x.pop_at_position(6))
    try:
        x.pop_at_position(14)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('khan', x.pop_at_position(2))
    try:
        x.pop_at_position(9)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('decor', x.pop_at_position(5))
    try:
        x.pop_at_position(11)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Isabel', x.pop_at_position(2))
    try:
        x.pop_at_position(7)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('hetero', x.pop_at_position(2))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Sunbelt', x.pop_at_position(2))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('NDjamena', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('polymer', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('superfluity')
    x.add('biological')
    x.add('TEFL')
    x.add('putsch')
    x.add('calibrate')
    x.add('Pace')
    test('Pace', x.pop_at_position(0))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('superfluity', x.pop_at_position(4))
    try:
        x.pop_at_position(9)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('calibrate', x.pop_at_position(0))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('TEFL', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('biological', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('putsch', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('beautification')
    x.add('nonintellectual')
    x.add('McVeigh')
    x.add('onerous')
    test('nonintellectual', x.pop_at_position(2))
    try:
        x.pop_at_position(6)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('onerous', x.pop_at_position(0))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('beautification', x.pop_at_position(1))
    try:
        x.pop_at_position(3)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('McVeigh', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('tideland')
    x.add('Fotomat')
    x.add('repertoire')
    x.add('commutative')
    test('repertoire', x.pop_at_position(1))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('tideland', x.pop_at_position(2))
    try:
        x.pop_at_position(5)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('commutative', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('Fotomat', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    x = LinkedList()
    x.add('stainless')
    x.add('pause')
    x.add('duct')
    x.add('tintype')
    x.add('unoriginal')
    test('pause', x.pop_at_position(3))
    try:
        x.pop_at_position(8)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('unoriginal', x.pop_at_position(0))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('duct', x.pop_at_position(1))
    try:
        x.pop_at_position(4)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('tintype', x.pop_at_position(0))
    try:
        x.pop_at_position(2)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)
    test('stainless', x.pop_at_position(0))
    try:
        x.pop_at_position(1)
        test(ValueError('ValueError'),'no error')
    except ValueError as err:
        test(True,True)

    print("Testing for Big O time: ")
    sizes = [1000, 10000, 100000, 1000000]

    for size in sizes:
        ll = LinkedList()
        lst = []
        
        # Test adding to front
        start = time.time()
        for i in range(size):
            ll.insert(0, i)
        end = time.time()
        print(f"LinkedList insert(0, item) for {size}: {end - start:.4f} sec")
        
        start = time.time()
        for i in range(size):
            lst.insert(0, i)
        end = time.time()
        print(f"Python list insert(0, item) for {size}: {end - start:.4f} sec")
        print("\n")
        
        # Test removing from front
        start = time.time()
        for i in range(size):
            ll.pop_at_position(0)
        end = time.time()
        print(f"LinkedList pop_at_position(0) for {size}: {end - start:.4f} sec")
        
        start = time.time()
        for i in range(size):
            lst.pop(0)
        end = time.time()
        print(f"Python list pop(0) for {size}: {end - start:.4f} sec")
        print("\n")
        
        # Test adding to end
        start = time.time()
        for i in range(size):
            ll.append(i)
        end = time.time()
        print(f"LinkedList append(item) for {size}: {end - start:.4f} sec")
        
        start = time.time()
        for i in range(size):
            lst.append(i)
        end = time.time()
        print(f"Python list append(item) for {size}: {end - start:.4f} sec")
        print("\n")
        
        # Test removing from end
        start = time.time()
        for i in range(size):
            ll.pop()
        end = time.time()
        print(f"LinkedList pop() for {size}: {end - start:.4f} sec")
        
        start = time.time()
        for i in range(size):
            lst.pop()
        end = time.time()
        print(f"Python list pop() for {size}: {end - start:.4f} sec")
        print("\n")


test_suite()