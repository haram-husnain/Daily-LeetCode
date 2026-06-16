def british_to_american(sentence):
    b2a_conversion = {
        "colour": "color", 
        "flavour": "flavor",
        "honour": "honor",
        "neighbour": "neighbor",
        "labour": "labor",
        "humour": "humor",
        "centre": "center",
        "fibre": "fiber",
        "defence": "defense",
        "offence": "offense",
        "organis": "organiz",
        "recognis": "recogniz",
        "analys": "analyz"
    }

    for british, american in b2a_conversion.items():
        british_cap = british.capitalize()
        british_upp = british.upper()
        american_cap = american.capitalize()
        american_upp = american.upper()

        sentence = sentence.replace(british, american)
        sentence = sentence.replace(british_cap, american_cap)
        sentence = sentence.replace(british_upp, american_upp)
    print(sentence)
    return sentence

test = british_to_american("The offence analysed, with organisation, the defence centre and recognised that the neighbouring labouror was humourous, flavourful, and colourful.") == "The offense analyzed, with organisation, the defense center and recognized that the neighboring laboror was humorous, flavorful, and colorful."
print(test)


#Given a sentence, convert any British English spellings to their American English equivalents using the following lookup table and return the updated sentence:
#British	American    #"analyse"	"analyze"
#"colour"	"color"    #"flavour"	"flavor"    #"honour"	"honor"     #"neighbour"	"neighbor"
#"labour"	"labor"     #"humour"	"humor"     #"centre"	"center"    #"fibre"	"fiber"     
#"defence"	"defense"   #"offence"	"offense"   #"organise"	"organize"      #"recognise"	"recognize"
#Replacements should be case-insensitive. For example, "Colour" should become "Color".
#The input may contain words that build on the exact spelling of a root in the table that also need to be changed. For example, "colouring" should become "coloring", and "disorganised" should become "disorganized".