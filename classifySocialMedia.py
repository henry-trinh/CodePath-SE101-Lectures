#Training Set = [Facebook, Instagram, Twitter, Linkedin, Snapchat, Pinterest]
#Testing Set = [TBA]

#Collaborated with Imani Musembi

intent = input("Personal or Professional? ")

if intent.title() == "Personal":
  question = input("Platonic or Romantic? ") 
  if question.title() == "Platonic":
    pictures = input("Are pictures the main focus? Yes or No. ")
    if pictures.lower() == "yes":
      print("We think you'd love Instagram!")
    else:
      print("Consider giving Twitter or Reddit a try!")
  else:
    preference = input("Are you part of the LGBTQ+ community? Yes or No. ")
    if preference.lower() == "yes":
      print("You should use Tinder!")
    else:
      print("Grindr and Her are cool apps!")
  #Intent
else: #Professional
  channels = input("Would you prefer separate channels to discuss different topics? Yes or No. ")
  if channels.lower() == "yes":
    print("You should download Slack!")
  else:
    print("I think you'd like LinkedIn.")