vertices_number = 468

def get_face_mesh(width, height, depth):

    vertices = [(0.000000, -0.034064, 0.059795), (0.000000, -0.011269, 0.074756), (0.000000, -0.020890, 0.060583), (-0.004639, 0.009554, 0.066336), (0.000000, -0.004632, 0.075866), (0.000000, 0.003657, 0.072429), (0.000000, 0.024733, 0.057886), (-0.042531, 0.025776, 0.032797), (0.000000, 0.040190, 0.052848), (0.000000, 0.048860, 0.053853), (0.000000, 0.082618, 0.044815), (0.000000, -0.037068, 0.058649), (0.000000, -0.039183, 0.055694), (0.000000, -0.039944, 0.052195), (0.000000, -0.045424, 0.054048), (0.000000, -0.047456, 0.055295), (0.000000, -0.050196, 0.056014), (0.000000, -0.053651, 0.055354), (0.000000, -0.061496, 0.050714), (0.000000, -0.015011, 0.071122), (-0.004161, -0.014664, 0.064477), (-0.070880, 0.054348, 0.000996), (-0.026286, 0.020359, 0.038481), (-0.031984, 0.019858, 0.037970), (-0.037752, 0.020394, 0.036462), (-0.044658, 0.024229, 0.031552), (-0.021643, 0.021899, 0.038518), (-0.032082, 0.032239, 0.041158), (-0.026738, 0.032053, 0.040922), (-0.037452, 0.031653, 0.039724), (-0.041610, 0.030591, 0.037196), (-0.050620, 0.019344, 0.027761), (-0.022667, -0.074258, 0.043898), (-0.044459, 0.026640, 0.031734), (-0.072145, 0.022630, 0.000731), (-0.057998, 0.023495, 0.022041), (-0.028449, -0.007209, 0.044331), (-0.007115, -0.033294, 0.058770), (-0.006060, -0.039246, 0.054449), (-0.014316, -0.035010, 0.054962), (-0.019149, -0.038031, 0.050289), (-0.011310, -0.039739, 0.051896), (-0.015635, -0.040828, 0.048423), (-0.026501, -0.050036, 0.041885), (-0.004270, -0.010941, 0.073605), (-0.004964, -0.004757, 0.074404), (-0.052533, 0.038816, 0.033632), (-0.017187, 0.009746, 0.045584), (-0.016086, -0.009425, 0.058142), (-0.016513, -0.006109, 0.055813), (-0.047655, -0.007016, 0.035346), (-0.004783, 0.002958, 0.071010), (-0.037350, 0.045082, 0.045505), (-0.045886, 0.043020, 0.040485), (-0.062793, 0.066154, 0.014258), (-0.012209, 0.041422, 0.051060), (-0.021935, 0.031003, 0.040006), (-0.031026, -0.043530, 0.040959), (-0.067197, -0.047886, -0.017454), (-0.011938, -0.013068, 0.057377), (-0.007298, -0.015937, 0.058332), (-0.024562, -0.043426, 0.042839), (-0.022048, -0.043045, 0.041625), (-0.049859, 0.048025, 0.037520), (-0.015923, -0.012577, 0.054569), (-0.026445, 0.045247, 0.049216), (-0.027603, 0.051010, 0.050160), (-0.035240, 0.080060, 0.037292), (-0.055998, 0.057155, 0.027243), (-0.030639, 0.065661, 0.045300), (-0.057210, 0.042546, 0.028309), (-0.063744, 0.047856, 0.015917), (-0.006727, -0.036880, 0.057378), (-0.012626, -0.037877, 0.054178), (-0.017326, -0.039528, 0.050006), (-0.010436, -0.014650, 0.056625), (-0.023212, -0.043291, 0.042582), (-0.020568, -0.044777, 0.045209), (-0.021531, -0.042763, 0.040381), (-0.009469, -0.010352, 0.065123), (-0.014691, -0.040364, 0.046049), (-0.010243, -0.039899, 0.049267), (-0.005334, -0.039932, 0.051382), (-0.007697, -0.060954, 0.049859), (-0.006996, -0.052918, 0.054483), (-0.006697, -0.049498, 0.055096), (-0.006309, -0.046951, 0.054494), (-0.005832, -0.045180, 0.053399), (-0.015372, -0.044232, 0.047455), (-0.016156, -0.044759, 0.048136), (-0.017291, -0.046187, 0.048545), (-0.018386, -0.048287, 0.048237), (-0.023682, -0.031062, 0.048681), (-0.075422, -0.010493, -0.024313), (0.000000, -0.017240, 0.066014), (-0.018266, -0.043995, 0.043990), (-0.019296, -0.044118, 0.044971), (-0.005974, -0.020137, 0.058665), (-0.014056, -0.017142, 0.052411), (-0.006624, -0.018193, 0.058638), (-0.023423, 0.005722, 0.042943), (-0.033273, 0.001049, 0.041139), (-0.017262, -0.009192, 0.052734), (-0.051332, 0.074856, 0.026604), (-0.045386, 0.063199, 0.036834), (-0.039866, 0.051095, 0.044663), (-0.021697, -0.054404, 0.044559), (-0.013956, 0.050120, 0.053160), (-0.016195, 0.065992, 0.049211), (-0.018914, 0.082364, 0.042750), (-0.041958, 0.022352, 0.033751), (-0.057333, 0.014117, 0.024317), (-0.018599, 0.023558, 0.038432), (-0.049886, 0.030747, 0.030839), (-0.013033, 0.014165, 0.048311), (-0.013058, -0.006728, 0.064160), (-0.064652, 0.009371, 0.016899), (-0.052587, 0.009458, 0.029743), (-0.044323, 0.007221, 0.035226), (-0.033007, 0.008616, 0.038728), (-0.024302, 0.011315, 0.040390), (-0.018207, 0.014680, 0.042241), (-0.005632, 0.023077, 0.055668), (-0.063381, -0.005293, 0.018812), (-0.055877, 0.032081, 0.026878), (-0.002426, -0.014629, 0.070715), (-0.016113, 0.003393, 0.048954), (-0.077431, 0.023650, -0.020052), (-0.013911, 0.018510, 0.044490), (-0.017858, -0.009783, 0.048505), (-0.046710, 0.026645, 0.030841), (-0.013340, -0.002838, 0.060970), (-0.072709, -0.028909, -0.022525), (-0.018564, 0.025852, 0.037579), (-0.009234, 0.000731, 0.066719), (-0.050006, -0.061351, 0.018925), (-0.050853, -0.071786, 0.007147), (-0.071593, -0.008118, -0.000720), (-0.058431, -0.052480, 0.009241), (-0.068473, 0.036629, 0.007247), (-0.024129, -0.082589, 0.041192), (-0.001799, -0.016899, 0.065733), (-0.021037, -0.001639, 0.045661), (-0.064076, 0.022360, 0.015608), (-0.036701, 0.023602, 0.036352), (-0.031772, 0.022943, 0.037757), (-0.021961, -0.045983, 0.044798), (-0.062349, -0.019444, 0.016635), (-0.012929, -0.092959, 0.040941), (-0.032107, -0.085333, 0.028020), (-0.040689, -0.079931, 0.019251), (0.000000, 0.065454, 0.050273), (0.000000, -0.094034, 0.042645), (-0.027240, 0.023158, 0.037772), (-0.022885, 0.023989, 0.036976), (-0.019983, 0.024965, 0.036891), (-0.061300, 0.033993, 0.020385), (-0.022885, 0.028865, 0.037750), (-0.027240, 0.029618, 0.038718), (-0.031772, 0.029641, 0.038770), (-0.036701, 0.029277, 0.037243), (-0.040184, 0.028574, 0.034830), (-0.075558, 0.041068, -0.009919), (-0.040184, 0.024837, 0.034409), (0.000000, -0.025219, 0.059323), (-0.017762, -0.026839, 0.052131), (-0.012222, -0.011824, 0.059525), (-0.007315, -0.025367, 0.058153), (0.000000, 0.032710, 0.052360), (-0.041353, -0.069966, 0.026720), (-0.033118, -0.076608, 0.033830), (-0.013137, -0.086400, 0.047025), (-0.059405, -0.062236, -0.006315), (-0.019983, 0.027438, 0.037440), (-0.009014, 0.012370, 0.057543), (0.000000, -0.087652, 0.048914), (-0.023090, -0.089742, 0.036091), (-0.069542, -0.024398, -0.001312), (-0.010988, -0.044588, 0.051207), (-0.011811, -0.045800, 0.051896), (-0.012558, -0.047879, 0.052371), (-0.013251, -0.051065, 0.052050), (-0.015464, -0.058194, 0.047579), (-0.019538, -0.041839, 0.044317), (-0.021178, -0.041371, 0.045551), (-0.022853, -0.040512, 0.045824), (-0.028502, -0.036657, 0.044850), (-0.052785, -0.022389, 0.028612), (-0.009467, 0.019076, 0.051968), (-0.013142, 0.031049, 0.042314), (-0.017800, 0.028600, 0.038816), (-0.018451, -0.040989, 0.042473), (-0.054362, -0.040305, 0.021099), (-0.007664, 0.031821, 0.048615), (-0.019386, -0.066144, 0.045211), (0.000000, 0.010594, 0.067746), (-0.005166, 0.015836, 0.061484), (0.000000, 0.017284, 0.063167), (-0.012468, 0.002303, 0.056810), (0.000000, -0.079422, 0.051812), (0.000000, -0.069915, 0.051535), (-0.009978, -0.069309, 0.049796), (-0.032888, -0.053825, 0.037958), (-0.023116, -0.015662, 0.045901), (-0.026803, -0.061116, 0.040962), (-0.038329, -0.015373, 0.041377), (-0.029619, -0.022742, 0.044409), (-0.043869, -0.026833, 0.036439), (-0.012173, -0.078345, 0.049693), (-0.015424, -0.001368, 0.052010), (-0.038784, -0.060418, 0.033111), (-0.030840, -0.068098, 0.038142), (-0.037473, -0.045035, 0.037265), (-0.060941, -0.032060, 0.014735), (-0.045890, -0.047287, 0.029832), (-0.065832, -0.039413, 0.000703), (-0.034926, -0.031958, 0.041302), (-0.012555, 0.008023, 0.053076), (-0.011261, -0.009336, 0.065388), (-0.014431, -0.011428, 0.059051), (-0.009230, -0.005290, 0.070034), (-0.017554, 0.035291, 0.043277), (-0.026326, 0.037138, 0.043646), (-0.033881, 0.037220, 0.043090), (-0.040758, 0.036754, 0.040761), (-0.046229, 0.034747, 0.036463), (-0.051718, 0.025358, 0.026709), (-0.072973, 0.007632, -0.000488), (-0.047068, 0.016510, 0.031095), (-0.040717, 0.014768, 0.034769), (-0.032698, 0.014707, 0.037319), (-0.025276, 0.016173, 0.038654), (-0.019709, 0.018585, 0.039618), (-0.015795, 0.020979, 0.040850), (-0.076642, 0.006731, -0.024359), (-0.013970, -0.013401, 0.056304), (-0.008848, 0.006587, 0.062332), (-0.007671, -0.009680, 0.070779), (-0.004602, -0.013341, 0.067874), (-0.007486, -0.010680, 0.067983), (-0.012364, -0.015856, 0.054805), (-0.003873, -0.014100, 0.069577), (-0.003199, -0.016079, 0.065087), (-0.016396, 0.025563, 0.038637), (-0.012556, 0.024671, 0.042038), (-0.010314, 0.023827, 0.046158), (-0.042531, 0.027723, 0.033153), (-0.045300, 0.029100, 0.033397), (0.004639, 0.009554, 0.066336), (0.042531, 0.025776, 0.032797), (0.004161, -0.014664, 0.064477), (0.070880, 0.054348, 0.000996), (0.026286, 0.020359, 0.038481), (0.031984, 0.019858, 0.037970), (0.037752, 0.020394, 0.036462), (0.044658, 0.024229, 0.031552), (0.021643, 0.021899, 0.038518), (0.032082, 0.032239, 0.041158), (0.026738, 0.032053, 0.040922), (0.037452, 0.031653, 0.039724), (0.041610, 0.030591, 0.037196), (0.050620, 0.019344, 0.027761), (0.022667, -0.074258, 0.043898), (0.044459, 0.026640, 0.031734), (0.072145, 0.022630, 0.000731), (0.057998, 0.023495, 0.022041), (0.028449, -0.007209, 0.044331), (0.007115, -0.033294, 0.058770), (0.006060, -0.039246, 0.054449), (0.014316, -0.035010, 0.054962), (0.019149, -0.038031, 0.050289), (0.011310, -0.039739, 0.051896), (0.015635, -0.040828, 0.048423), (0.026501, -0.050036, 0.041885), (0.004270, -0.010941, 0.073605), (0.004964, -0.004757, 0.074404), (0.052533, 0.038816, 0.033632), (0.017187, 0.009746, 0.045584), (0.016086, -0.009425, 0.058142), (0.016513, -0.006109, 0.055813), (0.047655, -0.007016, 0.035346), (0.004783, 0.002958, 0.071010), (0.037350, 0.045082, 0.045505), (0.045886, 0.043020, 0.040485), (0.062793, 0.066154, 0.014258), (0.012209, 0.041422, 0.051060), (0.021935, 0.031003, 0.040006), (0.031026, -0.043530, 0.040959), (0.067197, -0.047886, -0.017454), (0.011938, -0.013068, 0.057377), (0.007298, -0.015937, 0.058332), (0.024562, -0.043426, 0.042839), (0.022048, -0.043045, 0.041625), (0.049859, 0.048025, 0.037520), (0.015923, -0.012577, 0.054569), (0.026445, 0.045247, 0.049216), (0.027603, 0.051010, 0.050160), (0.035240, 0.080060, 0.037292), (0.055998, 0.057155, 0.027243), (0.030639, 0.065661, 0.045300), (0.057210, 0.042546, 0.028309), (0.063744, 0.047856, 0.015917), (0.006727, -0.036880, 0.057378), (0.012626, -0.037877, 0.054178), (0.017326, -0.039528, 0.050006), (0.010436, -0.014650, 0.056625), (0.023212, -0.043291, 0.042582), (0.020568, -0.044777, 0.045209), (0.021531, -0.042763, 0.040381), (0.009469, -0.010352, 0.065123), (0.014691, -0.040364, 0.046049), (0.010243, -0.039899, 0.049267), (0.005334, -0.039932, 0.051382), (0.007697, -0.060954, 0.049859), (0.006996, -0.052918, 0.054483), (0.006697, -0.049498, 0.055096), (0.006309, -0.046951, 0.054494), (0.005832, -0.045180, 0.053399), (0.015372, -0.044232, 0.047455), (0.016156, -0.044759, 0.048136), (0.017291, -0.046187, 0.048545), (0.018386, -0.048287, 0.048237), (0.023682, -0.031062, 0.048681), (0.075422, -0.010493, -0.024313), (0.018266, -0.043995, 0.043990), (0.019296, -0.044118, 0.044971), (0.005974, -0.020137, 0.058665), (0.014056, -0.017142, 0.052411), (0.006624, -0.018193, 0.058638), (0.023423, 0.005722, 0.042943), (0.033273, 0.001049, 0.041139), (0.017262, -0.009192, 0.052734), (0.051332, 0.074856, 0.026604), (0.045386, 0.063199, 0.036834), (0.039866, 0.051095, 0.044663), (0.021697, -0.054404, 0.044559), (0.013956, 0.050120, 0.053160), (0.016195, 0.065992, 0.049211), (0.018914, 0.082364, 0.042750), (0.041958, 0.022352, 0.033751), (0.057333, 0.014117, 0.024317), (0.018599, 0.023558, 0.038432), (0.049886, 0.030747, 0.030839), (0.013033, 0.014165, 0.048311), (0.013058, -0.006728, 0.064160), (0.064652, 0.009371, 0.016899), (0.052587, 0.009458, 0.029743), (0.044323, 0.007221, 0.035226), (0.033007, 0.008616, 0.038728), (0.024302, 0.011315, 0.040390), (0.018207, 0.014680, 0.042241), (0.005632, 0.023077, 0.055668), (0.063381, -0.005293, 0.018812), (0.055877, 0.032081, 0.026878), (0.002426, -0.014629, 0.070715), (0.016113, 0.003393, 0.048954), (0.077431, 0.023650, -0.020052), (0.013911, 0.018510, 0.044490), (0.017858, -0.009783, 0.048505), (0.046710, 0.026645, 0.030841), (0.013340, -0.002838, 0.060970), (0.072709, -0.028909, -0.022525), (0.018564, 0.025852, 0.037579), (0.009234, 0.000731, 0.066719), (0.050006, -0.061351, 0.018925), (0.050853, -0.071786, 0.007147), (0.071593, -0.008118, -0.000720), (0.058431, -0.052480, 0.009241), (0.068473, 0.036629, 0.007247), (0.024129, -0.082589, 0.041192), (0.001799, -0.016899, 0.065733), (0.021037, -0.001639, 0.045661), (0.064076, 0.022360, 0.015608), (0.036701, 0.023602, 0.036352), (0.031772, 0.022943, 0.037757), (0.021961, -0.045983, 0.044798), (0.062349, -0.019444, 0.016635), (0.012929, -0.092959, 0.040941), (0.032107, -0.085333, 0.028020), (0.040689, -0.079931, 0.019251), (0.027240, 0.023158, 0.037772), (0.022885, 0.023989, 0.036976), (0.019983, 0.024965, 0.036891), (0.061300, 0.033993, 0.020385), (0.022885, 0.028865, 0.037750), (0.027240, 0.029618, 0.038718), (0.031772, 0.029641, 0.038770), (0.036701, 0.029277, 0.037243), (0.040184, 0.028574, 0.034830), (0.075558, 0.041068, -0.009919), (0.040184, 0.024837, 0.034409), (0.017762, -0.026839, 0.052131), (0.012222, -0.011824, 0.059525), (0.007315, -0.025367, 0.058153), (0.041353, -0.069966, 0.026720), (0.033118, -0.076608, 0.033830), (0.013137, -0.086400, 0.047025), (0.059405, -0.062236, -0.006315), (0.019983, 0.027438, 0.037440), (0.009014, 0.012370, 0.057543), (0.023090, -0.089742, 0.036091), (0.069542, -0.024398, -0.001312), (0.010988, -0.044588, 0.051207), (0.011811, -0.045800, 0.051896), (0.012558, -0.047879, 0.052371), (0.013251, -0.051065, 0.052050), (0.015464, -0.058194, 0.047579), (0.019538, -0.041839, 0.044317), (0.021178, -0.041371, 0.045551), (0.022853, -0.040512, 0.045824), (0.028502, -0.036657, 0.044850), (0.052785, -0.022389, 0.028612), (0.009467, 0.019076, 0.051968), (0.013142, 0.031049, 0.042314), (0.017800, 0.028600, 0.038816), (0.018451, -0.040989, 0.042473), (0.054362, -0.040305, 0.021099), (0.007664, 0.031821, 0.048615), (0.019386, -0.066144, 0.045211), (0.005166, 0.015836, 0.061484), (0.012468, 0.002303, 0.056810), (0.009978, -0.069309, 0.049796), (0.032888, -0.053825, 0.037958), (0.023116, -0.015662, 0.045901), (0.026803, -0.061116, 0.040962), (0.038329, -0.015373, 0.041377), (0.029619, -0.022742, 0.044409), (0.043869, -0.026833, 0.036439), (0.012173, -0.078345, 0.049693), (0.015424, -0.001368, 0.052010), (0.038784, -0.060418, 0.033111), (0.030840, -0.068098, 0.038142), (0.037473, -0.045035, 0.037265), (0.060941, -0.032060, 0.014735), (0.045890, -0.047287, 0.029832), (0.065832, -0.039413, 0.000703), (0.034926, -0.031958, 0.041302), (0.012555, 0.008023, 0.053076), (0.011261, -0.009336, 0.065388), (0.014431, -0.011428, 0.059051), (0.009230, -0.005290, 0.070034), (0.017554, 0.035291, 0.043277), (0.026326, 0.037138, 0.043646), (0.033881, 0.037220, 0.043090), (0.040758, 0.036754, 0.040761), (0.046229, 0.034747, 0.036463), (0.051718, 0.025358, 0.026709), (0.072973, 0.007632, -0.000488), (0.047068, 0.016510, 0.031095), (0.040717, 0.014768, 0.034769), (0.032698, 0.014707, 0.037319), (0.025276, 0.016173, 0.038654), (0.019709, 0.018585, 0.039618), (0.015795, 0.020979, 0.040850), (0.076642, 0.006731, -0.024359), (0.013970, -0.013401, 0.056304), (0.008848, 0.006587, 0.062332), (0.007671, -0.009680, 0.070779), (0.004602, -0.013341, 0.067874), (0.007486, -0.010680, 0.067983), (0.012364, -0.015856, 0.054805), (0.003873, -0.014100, 0.069577), (0.003199, -0.016079, 0.065087), (0.016396, 0.025563, 0.038637), (0.012556, 0.024671, 0.042038), (0.010314, 0.023827, 0.046158), (0.042531, 0.027723, 0.033153), (0.045300, 0.029100, 0.033397)]

    faces = [(174, 156, 134), (247, 34, 8), (383, 399, 363), (264, 467, 250), (309, 416, 325), (79, 96, 192), (357, 390, 265), (128, 35, 163), (369, 265, 390), (140, 163, 35), (268, 1, 303), (38, 73, 1), (12, 303, 1), (12, 1, 73), (350, 452, 351), (121, 122, 232), (453, 351, 452), (233, 232, 122), (268, 303, 270), (38, 40, 73), (304, 270, 303), (74, 73, 40), (358, 344, 351), (129, 122, 115), (278, 351, 344), (48, 115, 122), (351, 453, 358), (122, 129, 233), (454, 358, 453), (234, 233, 129), (300, 334, 298), (70, 68, 105), (333, 298, 334), (104, 105, 68), (176, 153, 397), (176, 172, 153), (378, 397, 153), (149, 153, 172), (382, 385, 383), (155, 156, 158), (399, 383, 385), (174, 158, 156), (281, 348, 331), (51, 102, 119), (349, 331, 348), (120, 119, 102), (270, 304, 271), (40, 41, 74), (305, 271, 304), (75, 74, 41), (10, 337, 152), (10, 152, 108), (338, 152, 337), (109, 108, 152), (345, 279, 361), (116, 132, 49), (280, 361, 279), (50, 49, 132), (263, 432, 419), (33, 195, 212), (425, 419, 432), (205, 212, 195), (305, 409, 271), (75, 41, 185), (410, 271, 409), (186, 185, 41), (273, 311, 408), (43, 184, 81), (416, 408, 311), (192, 81, 184), (323, 271, 411), (93, 187, 41), (410, 411, 271), (186, 41, 187), (348, 450, 349), (119, 120, 230), (451, 349, 450), (231, 230, 120), (435, 433, 431), (215, 211, 213), (423, 431, 433), (203, 213, 211), (314, 315, 19), (84, 19, 85), (18, 19, 315), (18, 85, 19), (308, 376, 307), (78, 77, 147), (292, 307, 376), (62, 147, 77), (260, 388, 261), (30, 31, 161), (389, 261, 388), (162, 161, 31), (287, 415, 385), (57, 158, 191), (399, 385, 415), (174, 191, 158), (419, 425, 407), (195, 183, 205), (336, 407, 425), (107, 205, 183), (368, 417, 365), (139, 136, 193), (435, 365, 417), (215, 193, 136), (392, 424, 328), (166, 99, 204), (359, 328, 424), (130, 204, 99), (299, 302, 285), (69, 55, 72), (252, 285, 302), (22, 72, 55), (5, 276, 6), (5, 6, 46), (282, 6, 276), (52, 46, 6), (255, 374, 254), (25, 24, 145), (375, 254, 374), (146, 145, 24), (321, 322, 308), (91, 78, 92), (376, 308, 322), (147, 92, 78), (281, 426, 412), (51, 188, 206), (428, 412, 426), (208, 206, 188), (422, 314, 201), (202, 201, 84), (19, 201, 314), (19, 84, 201), (336, 322, 407), (107, 183, 92), (406, 407, 322), (182, 92, 183), (406, 322, 405), (182, 181, 92), (321, 405, 322), (91, 92, 181), (18, 315, 17), (18, 17, 85), (316, 17, 315), (86, 85, 17), (426, 267, 427), (206, 207, 37), (424, 427, 267), (204, 37, 207), (370, 397, 401), (141, 177, 172), (378, 401, 397), (149, 172, 177), (392, 270, 323), (166, 93, 40), (271, 323, 270), (41, 40, 93), (418, 466, 414), (194, 190, 246), (465, 414, 466), (245, 246, 190), (258, 259, 387), (28, 160, 29), (386, 387, 259), (159, 29, 160), (261, 389, 468), (31, 248, 162), (467, 468, 389), (247, 162, 248), (249, 457, 420), (4, 197, 237), (400, 420, 457), (175, 237, 197), (334, 299, 333), (105, 104, 69), (285, 333, 299), (55, 69, 104), (286, 9, 418), (56, 194, 9), (169, 418, 9), (169, 9, 194), (341, 262, 347), (112, 118, 32), (449, 347, 262), (229, 32, 118), (286, 418, 442), (56, 222, 194), (414, 442, 418), (190, 194, 222), (328, 461, 327), (99, 98, 241), (329, 327, 461), (100, 241, 98), (278, 356, 330), (48, 101, 127), (372, 330, 356), (143, 127, 101), (310, 393, 439), (80, 219, 167), (440, 439, 393), (220, 167, 219), (382, 383, 257), (155, 27, 156), (342, 257, 383), (113, 156, 27), (361, 280, 421), (132, 199, 50), (430, 421, 280), (210, 50, 199), (366, 365, 380), (137, 151, 136), (395, 380, 365), (170, 136, 151), (356, 278, 438), (127, 218, 48), (344, 438, 278), (115, 48, 218), (444, 445, 283), (224, 53, 225), (284, 283, 445), (54, 225, 53), (282, 276, 364), (52, 135, 46), (441, 364, 276), (221, 46, 135), (432, 263, 396), (212, 171, 33), (370, 396, 263), (141, 33, 171), (338, 300, 339), (109, 110, 70), (298, 339, 300), (68, 70, 110), (336, 274, 322), (107, 92, 44), (376, 322, 274), (147, 44, 92), (349, 451, 350), (120, 121, 231), (452, 350, 451), (232, 231, 121), (468, 360, 343), (248, 114, 131), (447, 343, 360), (227, 131, 114), (283, 284, 335), (53, 106, 54), (294, 335, 284), (64, 54, 106), (251, 459, 463), (21, 243, 239), (462, 463, 459), (242, 239, 243), (277, 354, 301), (47, 71, 125), (384, 301, 354), (157, 125, 71), (326, 293, 325), (97, 96, 63), (309, 325, 293), (79, 63, 96), (284, 277, 294), (54, 64, 47), (301, 294, 277), (71, 47, 64), (448, 265, 346), (228, 117, 35), (373, 346, 265), (144, 35, 117), (353, 346, 347), (124, 118, 117), (341, 347, 346), (112, 117, 118), (2, 20, 275), (2, 45, 20), (355, 275, 20), (126, 20, 45), (249, 282, 457), (4, 237, 52), (364, 457, 282), (135, 52, 237), (426, 427, 428), (206, 208, 207), (437, 428, 427), (217, 207, 208), (381, 382, 253), (154, 23, 155), (257, 253, 382), (27, 155, 23), (392, 394, 270), (166, 40, 168), (268, 270, 394), (38, 168, 40), (200, 429, 201), (200, 201, 209), (422, 201, 429), (202, 209, 201), (331, 330, 267), (102, 37, 101), (372, 267, 330), (143, 101, 37), (423, 433, 274), (203, 44, 213), (288, 274, 433), (58, 213, 44), (291, 251, 329), (61, 100, 21), (463, 329, 251), (243, 21, 100), (259, 287, 386), (29, 159, 57), (385, 386, 287), (158, 57, 159), (343, 447, 354), (114, 125, 227), (266, 354, 447), (36, 227, 125), (258, 387, 260), (28, 30, 160), (388, 260, 387), (161, 160, 30), (431, 423, 432), (211, 212, 203), (425, 432, 423), (205, 203, 212), (446, 343, 277), (226, 47, 114), (354, 277, 343), (125, 114, 47), (425, 423, 336), (205, 107, 203), (274, 336, 423), (44, 203, 107), (307, 293, 308), (77, 78, 63), (326, 308, 293), (97, 63, 78), (367, 448, 353), (138, 124, 228), (346, 353, 448), (117, 228, 124), (303, 269, 304), (73, 74, 39), (272, 304, 269), (42, 39, 74), (372, 359, 267), (143, 37, 130), (424, 267, 359), (204, 130, 37), (328, 295, 461), (99, 241, 65), (456, 461, 295), (236, 65, 241), (295, 332, 279), (65, 49, 103), (280, 279, 332), (50, 103, 49), (304, 272, 305), (74, 75, 42), (273, 305, 272), (43, 42, 75), (428, 437, 435), (208, 215, 217), (433, 435, 437), (213, 217, 215), (305, 273, 409), (75, 185, 43), (408, 409, 273), (184, 43, 185), (395, 431, 396), (170, 171, 211), (432, 396, 431), (212, 211, 171), (396, 370, 379), (171, 150, 141), (401, 379, 370), (177, 141, 150), (297, 335, 300), (67, 70, 106), (334, 300, 335), (105, 106, 70), (418, 169, 352), (194, 123, 169), (7, 352, 169), (7, 169, 123), (281, 412, 353), (51, 124, 188), (377, 353, 412), (148, 188, 124), (320, 321, 326), (90, 97, 91), (308, 326, 321), (78, 91, 97), (286, 296, 337), (56, 108, 66), (297, 337, 296), (67, 66, 108), (405, 321, 404), (181, 180, 91), (320, 404, 321), (90, 91, 180), (331, 349, 330), (102, 101, 120), (350, 330, 349), (121, 120, 101), (335, 294, 334), (106, 105, 64), (299, 334, 294), (69, 64, 105), (324, 455, 367), (94, 138, 235), (448, 367, 455), (228, 235, 138), (17, 316, 16), (17, 16, 86), (317, 16, 316), (87, 86, 16), (430, 280, 359), (210, 130, 50), (332, 359, 280), (103, 50, 130), (16, 317, 15), (16, 15, 87), (318, 15, 317), (88, 87, 15), (9, 286, 10), (9, 10, 56), (337, 10, 286), (108, 56, 10), (330, 350, 278), (101, 48, 121), (351, 278, 350), (122, 121, 48), (253, 254, 381), (23, 154, 24), (375, 381, 254), (146, 24, 154), (403, 404, 319), (179, 89, 180), (320, 319, 404), (90, 180, 89), (352, 7, 420), (123, 197, 7), (198, 420, 7), (198, 7, 197), (325, 319, 326), (96, 97, 89), (320, 326, 319), (90, 89, 97), (398, 368, 366), (173, 137, 139), (365, 366, 368), (136, 139, 137), (289, 436, 398), (59, 173, 216), (368, 398, 436), (139, 216, 173), (439, 440, 345), (219, 116, 220), (279, 345, 440), (49, 220, 116), (272, 312, 273), (42, 43, 82), (311, 273, 312), (81, 82, 43), (6, 282, 196), (6, 196, 52), (249, 196, 282), (4, 52, 196), (274, 288, 376), (44, 147, 58), (292, 376, 288), (62, 58, 147), (397, 429, 176), (172, 176, 209), (200, 176, 429), (200, 209, 176), (269, 313, 272), (39, 42, 83), (312, 272, 313), (82, 83, 42), (445, 446, 284), (225, 54, 226), (277, 284, 446), (47, 226, 54), (255, 340, 374), (25, 145, 111), (391, 374, 340), (164, 111, 145), (296, 283, 297), (66, 67, 53), (335, 297, 283), (106, 53, 67), (347, 449, 348), (118, 119, 229), (450, 348, 449), (230, 229, 119), (455, 357, 448), (235, 228, 128), (265, 448, 357), (35, 128, 228), (337, 297, 338), (108, 109, 67), (300, 338, 297), (70, 67, 109), (152, 338, 11), (152, 11, 109), (339, 11, 338), (110, 109, 11), (279, 440, 295), (49, 65, 220), (456, 295, 440), (236, 220, 65), (408, 416, 293), (184, 63, 192), (309, 293, 416), (79, 192, 63), (359, 372, 430), (130, 210, 143), (356, 430, 372), (127, 143, 210), (346, 373, 341), (117, 112, 144), (266, 341, 373), (36, 144, 112), (389, 391, 467), (162, 247, 164), (250, 467, 391), (8, 164, 247), (353, 347, 281), (124, 51, 118), (348, 281, 347), (119, 118, 51), (296, 443, 283), (66, 53, 223), (444, 283, 443), (224, 223, 53), (20, 95, 355), (20, 126, 95), (371, 355, 95), (142, 95, 126), (296, 286, 443), (66, 223, 56), (442, 443, 286), (222, 56, 223), (420, 198, 249), (197, 4, 198), (196, 249, 198), (196, 198, 4), (360, 264, 256), (131, 26, 34), (250, 256, 264), (8, 34, 26), (276, 275, 441), (46, 221, 45), (458, 441, 275), (238, 45, 221), (301, 384, 302), (71, 72, 157), (369, 302, 384), (140, 157, 72), (418, 352, 466), (194, 246, 123), (413, 466, 352), (189, 123, 246), (467, 264, 468), (247, 248, 34), (360, 468, 264), (131, 34, 248), (390, 252, 369), (163, 140, 22), (302, 369, 252), (72, 22, 140), (375, 387, 381), (146, 154, 160), (386, 381, 387), (159, 160, 154), (380, 395, 379), (151, 150, 170), (396, 379, 395), (171, 170, 150), (352, 420, 413), (123, 189, 197), (400, 413, 420), (175, 197, 189), (427, 323, 437), (207, 217, 93), (411, 437, 323), (187, 93, 217), (388, 374, 389), (161, 162, 145), (391, 389, 374), (164, 145, 162), (394, 327, 165), (168, 165, 98), (3, 165, 327), (3, 98, 165), (355, 371, 462), (126, 242, 142), (463, 462, 371), (243, 142, 242), (1, 268, 165), (1, 165, 38), (394, 165, 268), (168, 38, 165), (12, 13, 303), (12, 73, 13), (269, 303, 13), (39, 13, 73), (387, 375, 388), (160, 161, 146), (374, 388, 375), (145, 146, 161), (13, 14, 269), (13, 39, 14), (313, 269, 14), (83, 14, 39), (294, 301, 299), (64, 69, 71), (302, 299, 301), (72, 71, 69), (341, 266, 262), (112, 32, 36), (447, 262, 266), (227, 36, 32), (381, 386, 382), (154, 155, 159), (385, 382, 386), (158, 159, 155), (281, 331, 426), (51, 206, 102), (267, 426, 331), (37, 102, 206), (424, 392, 427), (204, 207, 166), (323, 427, 392), (93, 166, 207), (430, 356, 421), (210, 199, 127), (438, 421, 356), (218, 127, 199), (392, 328, 394), (166, 168, 99), (327, 394, 328), (98, 99, 168), (458, 439, 441), (238, 221, 219), (345, 441, 439), (116, 219, 221), (383, 363, 342), (156, 113, 134), (464, 342, 363), (244, 134, 113), (458, 462, 460), (238, 240, 242), (459, 460, 462), (239, 242, 240), (435, 431, 365), (215, 136, 211), (395, 365, 431), (170, 211, 136), (415, 464, 399), (191, 174, 244), (363, 399, 464), (134, 244, 174), (263, 429, 370), (33, 141, 209), (397, 370, 429), (172, 209, 141), (458, 275, 462), (238, 242, 45), (355, 462, 275), (126, 45, 242), (317, 404, 318), (87, 88, 180), (403, 318, 404), (179, 180, 88), (316, 405, 317), (86, 87, 181), (404, 317, 405), (180, 181, 87), (315, 406, 316), (85, 86, 182), (405, 316, 406), (181, 182, 86), (314, 407, 315), (84, 85, 183), (406, 315, 407), (182, 183, 85), (419, 407, 422), (195, 202, 183), (314, 422, 407), (84, 183, 202), (367, 402, 324), (138, 94, 178), (362, 324, 402), (133, 178, 94), (409, 408, 307), (185, 77, 184), (293, 307, 408), (63, 184, 77), (409, 307, 410), (185, 186, 77), (292, 410, 307), (62, 77, 186), (411, 410, 288), (187, 58, 186), (292, 288, 410), (62, 186, 58), (437, 411, 433), (217, 213, 187), (288, 433, 411), (58, 187, 213), (435, 417, 428), (215, 208, 193), (412, 428, 417), (188, 193, 208), (265, 369, 373), (35, 144, 140), (384, 373, 369), (157, 140, 144), (458, 460, 439), (238, 219, 240), (310, 439, 460), (80, 240, 219), (353, 377, 367), (124, 138, 148), (402, 367, 377), (178, 148, 138), (5, 2, 276), (5, 46, 2), (275, 276, 2), (45, 2, 46), (429, 263, 422), (209, 202, 33), (419, 422, 263), (195, 33, 202), (328, 359, 295), (99, 65, 130), (332, 295, 359), (103, 130, 65), (368, 436, 417), (139, 193, 216), (434, 417, 436), (214, 216, 193), (456, 440, 290), (236, 60, 220), (393, 290, 440), (167, 220, 60), (329, 463, 327), (100, 98, 243), (371, 327, 463), (142, 243, 98), (327, 371, 3), (98, 3, 142), (95, 3, 371), (95, 142, 3), (461, 456, 306), (241, 76, 236), (290, 306, 456), (60, 236, 76), (449, 340, 450), (229, 230, 111), (255, 450, 340), (25, 111, 230), (262, 447, 256), (32, 26, 227), (360, 256, 447), (131, 227, 26), (450, 255, 451), (230, 231, 25), (254, 451, 255), (24, 25, 231), (451, 254, 452), (231, 232, 24), (253, 452, 254), (23, 24, 232), (452, 253, 453), (232, 233, 23), (257, 453, 253), (27, 23, 233), (257, 342, 453), (27, 233, 113), (454, 453, 342), (234, 113, 233), (414, 465, 415), (190, 191, 245), (464, 415, 465), (244, 245, 191), (442, 414, 287), (222, 57, 190), (415, 287, 414), (191, 190, 57), (442, 287, 443), (222, 223, 57), (259, 443, 287), (29, 57, 223), (443, 259, 444), (223, 224, 29), (258, 444, 259), (28, 29, 224), (445, 444, 260), (225, 30, 224), (258, 260, 444), (28, 224, 30), (260, 261, 445), (30, 225, 31), (446, 445, 261), (226, 31, 225), (261, 468, 446), (31, 226, 248), (343, 446, 468), (114, 248, 226), (251, 310, 459), (21, 239, 80), (460, 459, 310), (240, 80, 239), (291, 306, 393), (61, 167, 76), (290, 393, 306), (60, 76, 167), (461, 306, 329), (241, 100, 76), (291, 329, 306), (61, 76, 100), (377, 434, 402), (148, 178, 214), (436, 402, 434), (216, 214, 178), (251, 291, 310), (21, 80, 61), (393, 310, 291), (167, 61, 80), (412, 417, 377), (188, 148, 193), (434, 377, 417), (214, 193, 148), (342, 464, 454), (113, 234, 244), (465, 454, 464), (245, 244, 234), (454, 465, 358), (234, 129, 245), (466, 358, 465), (246, 245, 129), (413, 344, 466), (189, 246, 115), (358, 466, 344), (129, 115, 246), (438, 344, 400), (218, 175, 115), (413, 400, 344), (189, 115, 175), (364, 441, 361), (135, 132, 221), (345, 361, 441), (116, 221, 132), (457, 421, 400), (237, 175, 199), (438, 400, 421), (218, 199, 175), (457, 364, 421), (237, 199, 135), (361, 421, 364), (132, 135, 199), (362, 402, 289), (133, 59, 178), (436, 289, 402), (216, 178, 59), (354, 266, 384), (125, 157, 36), (373, 384, 266), (144, 36, 157), (256, 250, 340), (26, 111, 8), (391, 340, 250), (164, 8, 111), (262, 256, 449), (32, 229, 26), (340, 449, 256), (111, 26, 229), (15, 318, 14), (15, 14, 88), (313, 14, 318), (83, 88, 14), (318, 403, 313), (88, 83, 179), (312, 313, 403), (82, 179, 83), (403, 319, 312), (179, 82, 89), (311, 312, 319), (81, 89, 82), (319, 325, 311), (89, 81, 96), (416, 311, 325), (192, 96, 81)]


    # apply size
    for i, v in enumerate(vertices):
        vertices[i] = v[0] * width,  - v[2] * height, v[1] * depth # 90 degrees X rotation
        
       
    return vertices, faces