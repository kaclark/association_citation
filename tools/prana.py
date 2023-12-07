#Surya Siddhanta
#Chapter 1 Of the Mean Motions of the Planets
#11
#That which begins with respirations (prana) is called real; 
#that which begins with atoms (truti) is called unreal.
#Six respirations make a vinadi.
#Sixty of these a nudi.
#12
#And sixty nadis make a sidreal day and night[~24 hours]
#footnote:
#10 long syllables (gurvakshara) == 1 respiration(prana, 4 seconds)
#6 respirations                  == 1 vinadi (24 seconds)
#60 vinadis                      == 1 nadi (24 minutes)
#60 nadis                        == 1 Day (24 hours)

conversion_scalar_map = {
    "second": {"prana": (1/4),    "vinadi": (1/24),    "nadi": (1/1440)},
    "minute": {"prana": (60/4),   "vinadi": (60/24),   "nadi": (1/24)},
    "hour":   {"prana": (3600/4), "vinadi": (3600/24), "nadi": (60/24)},

    "prana":  {"second": 4,       "minute": (4/60),    "hour": (4/3600)},
    "vinadi": {"second": 24,      "minute": (24/60),   "hour": (24/3600)},
    "nadi":   {"second": 1440,    "minute": 24,        "hour": (24/60)}
}
#usage value * conversion_scalar_map['unit_from']['unit_to']
#eg to find how many prana are within 5 minutes
#print(5*conversion_scalar_map["minute"]["prana"])

