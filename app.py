import streamlit as st
from gtts import gTTS
import os
import random

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="SanaEnglishPro V2", page_icon="🎓", layout="wide")

# 2. FONCTION AUDIO
def prononcer_anglais(texte):
    try:
        # Nettoyage du texte pour gTTS
        texte_propre = texte.split('(')[0].split('/')[0].split('—')[0].strip()
        tts = gTTS(text=texte_propre, lang='en')
        filename = "prononciation.mp3"
        tts.save(filename)
        with open(filename, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        os.remove(filename)
    except Exception:
        st.error("Erreur audio.")

# 3. BASE DE DONNÉES (Session State pour éviter de recharger)
if 'data' not in st.session_state:
    st.session_state.data = [
        # --- VIE QUOTIDIENNE & SALUTATIONS ---
        {"en": "What's up?", "fr": "Quoi de neuf ?", "ex": "Hey man, what's up?"},
        {"en": "How’s it going?", "fr": "Comment ça va ?", "ex": "How’s it going with your new job?"},
        {"en": "Long time no see", "fr": "Ça fait un bail", "ex": "Oh, hi Mark! Long time no see."},
        {"en": "Take care", "fr": "Prends soin de toi", "ex": "See you tomorrow, take care!"},
        {"en": "Have a good one", "fr": "Bonne journée", "ex": "Thanks, you have a good one too."},
        {"en": "I’m exhausted", "fr": "Je suis épuisé", "ex": "I worked 10 hours, I’m exhausted."},
        {"en": "I’m starving", "fr": "Je meurs de faim", "ex": "Let's eat, I'm starving."},
        {"en": "It’s up to you", "fr": "C’est toi qui décides", "ex": "Pizza or pasta? It’s up to you."},
        {"en": "I don’t mind", "fr": "Ça ne me dérange pas", "ex": "I don’t mind waiting."},
        {"en": "Never mind", "fr": "Laisse tomber / C’est pas grave", "ex": "Never mind, I found my keys."},
        {"en": "No worries", "fr": "Pas de souci", "ex": "You're late? No worries."},
        {"en": "What do you mean?", "fr": "Que veux-tu dire ?", "ex": "I don't understand, what do you mean?"},
        {"en": "I guess so", "fr": "Je suppose que oui", "ex": "Is it going to rain? I guess so."},
        {"en": "Check this out", "fr": "Regarde ça", "ex": "Check this out, it’s a new app."},
        {"en": "My bad", "fr": "C’est ma faute", "ex": "I forgot to call you, my bad."},
        {"en": "Anyway...", "fr": "Bref / De toute façon...", "ex": "Anyway, let’s talk about something else."},
        {"en": "To be honest...", "fr": "Pour être honnête...", "ex": "To be honest, I don't like this movie."},
        {"en": "Keep in touch", "fr": "On reste en contact", "ex": "Call me, let's keep in touch."},
        {"en": "Cheers!", "fr": "Santé / Merci / Salut", "ex": "Cheers for the help!"},
        {"en": "Make yourself at home", "fr": "Fais comme chez toi", "ex": "Come in and make yourself at home."},
        {"en": "You're welcome", "fr": "Je vous en prie / De rien", "ex": "Thanks for the gift! - You're welcome."},
        {"en": "I'm on my way", "fr": "Je suis en route", "ex": "Wait for me, I'm on my way."},
        {"en": "Hold on a second", "fr": "Attends une seconde", "ex": "Hold on, I'm on the phone."},
        {"en": "Give me a sec", "fr": "Donne-moi une seconde", "ex": "I'm busy, give me a sec."},
        {"en": "It doesn't matter", "fr": "Ça n'a pas d'importance", "ex": "It doesn't matter if you're late."},
        {"en": "I have no idea", "fr": "Je n'en ai aucune idée", "ex": "Where is he? - I have no idea."},
        {"en": "Can you help me?", "fr": "Peux-tu m'aider ?", "ex": "This is heavy, can you help me?"},
        {"en": "Don't worry about it", "fr": "Ne t'en fais pas pour ça", "ex": "I broke a glass. - Don't worry about it."},
        {"en": "I'm lost", "fr": "Je suis perdu", "ex": "I'm lost, where is the station?"},
        {"en": "Nice to meet you", "fr": "Ravi de vous rencontrer", "ex": "I'm John. - Nice to meet you."},

        # --- TRAVAIL & RÉUNION ---
        {"en": "Get down to business", "fr": "Passons aux choses sérieuses", "ex": "Let's get down to business."},
        {"en": "Keep me posted", "fr": "Tiens-moi au courant", "ex": "Keep me posted on the situation."},
        {"en": "In a nutshell", "fr": "En résumé", "ex": "In a nutshell, we are losing money."},
        {"en": "Think out of the box", "fr": "Penser différemment", "ex": "We need to think out of the box."},
        {"en": "Call it a day", "fr": "Finir sa journée", "ex": "It’s 6 PM, let’s call it a day."},
        {"en": "Work from home (WFH)", "fr": "Télétravail", "ex": "I work from home on Fridays."},
        {"en": "To be on the same page", "fr": "Être sur la même longueur d'onde", "ex": "We need to be on the same page."},
        {"en": "Back to square one", "fr": "Retour à la case départ", "ex": "The plan failed, back to square one."},
        {"en": "Win-win situation", "fr": "Situation gagnant-gagnant", "ex": "It's a win-win situation for us."},
        {"en": "Under the weather", "fr": "Un peu malade", "ex": "I'm feeling a bit under the weather today."},
        {"en": "Piece of cake", "fr": "C'est du gâteau / Très facile", "ex": "That exam was a piece of cake."},
        {"en": "The bottom line", "fr": "L'essentiel / Le résultat net", "ex": "The bottom line is we need more users."},
        {"en": "To meet a deadline", "fr": "Respecter une échéance", "ex": "We must meet the deadline."},
        {"en": "To schedule a meeting", "fr": "Planifier une réunion", "ex": "Can we schedule a meeting for Monday?"},
        {"en": "To follow up", "fr": "Faire un suivi", "ex": "I'll follow up with you tomorrow."},
        {"en": "As far as I'm concerned", "fr": "En ce qui me concerne", "ex": "As far as I'm concerned, it's a good plan."},
        {"en": "In the meantime", "fr": "En attendant", "ex": "Wait here, I'll be back in the meantime."},
        {"en": "I'm overwhelmed", "fr": "Je suis débordé", "ex": "I have too much work, I'm overwhelmed."},
        {"en": "Let's touch base", "fr": "Reprenons contact", "ex": "Let's touch base next week."},
        {"en": "I'll get back to you", "fr": "Je reviendrai vers vous", "ex": "I'll check and get back to you."},
        {"en": "It's a priority", "fr": "C'est une priorité", "ex": "This bug is a priority."},
        {"en": "Can we move on?", "fr": "Pouvons-nous avancer ?", "ex": "Enough about that, can we move on?"},
        {"en": "To summarize", "fr": "Pour résumer", "ex": "To summarize, the project is on track."},
        {"en": "I agree with you", "fr": "Je suis d'accord avec vous", "ex": "I agree with you on this point."},
        {"en": "I don't think so", "fr": "Je ne pense pas", "ex": "Is it easy? - I don't think so."},
        {"en": "That's a good point", "fr": "C'est un bon point", "ex": "You're right, that's a good point."},
        {"en": "Let's wrap it up", "fr": "Finissons-en / Concluons", "ex": "It's late, let's wrap it up."},
        {"en": "What do you think?", "fr": "Qu'en penses-tu ?", "ex": "I like it, what do you think?"},
        {"en": "Any questions?", "fr": "Des questions ?", "ex": "That's all, any questions?"},
        {"en": "To postpone", "fr": "Reporter", "ex": "The meeting is postponed to Friday."},
        {"en": "To cancel", "fr": "Annuler", "ex": "They cancelled the flight."},
        {"en": "Keep up the good work", "fr": "Continue ton bon travail", "ex": "Great results, keep up the good work!"},
        {"en": "To take care of", "fr": "S'occuper de", "ex": "I'll take care of the report."},
        {"en": "I'm in charge of...", "fr": "Je suis responsable de...", "ex": "I'm in charge of maintenance."},
        {"en": "To troubleshoot", "fr": "Dépanner / Résoudre", "ex": "I need to troubleshoot this site."},
        {"en": "Site audit", "fr": "Audit de site", "ex": "We are conducting a site audit."},
        {"en": "Power failure", "fr": "Panne d'électricité", "ex": "There is a power failure at site X."},
        {"en": "To alignment antennas", "fr": "Aligner les antennes", "ex": "You need to align the antennas properly."},
        {"en": "Microwave link", "fr": "Lien hertzien", "ex": "The microwave link is down."},
        {"en": "To perform a test", "fr": "Effectuer un test", "ex": "Let's perform a loop test."},

        # --- EMAILS & RÉDACTION ---
        {"en": "I hope this email finds you well", "fr": "J'espère que vous allez bien", "ex": "Dear Eric, I hope this email finds you well."},
        {"en": "Further to our conversation...", "fr": "Suite à notre conversation...", "ex": "Further to our conversation this morning..."},
        {"en": "Please find attached", "fr": "Veuillez trouver ci-joint", "ex": "Please find attached the report."},
        {"en": "Could you please clarify...?", "fr": "Pourriez-vous clarifier... ?", "ex": "Could you please clarify what you mean by that?"},
        {"en": "I look forward to hearing from you", "fr": "Dans l'attente de votre réponse", "ex": "I look forward to hearing from you soon."},
        {"en": "Best regards", "fr": "Cordialement", "ex": "Best regards, Rosly."},
        {"en": "Thank you for your prompt reply", "fr": "Merci pour votre réponse rapide", "ex": "Got it, thank you for your prompt reply."},
        {"en": "To whom it may concern", "fr": "À qui de droit", "ex": "To whom it may concern, I am writing to..."},
        {"en": "I am writing to inform you", "fr": "Je vous écris pour vous informer", "ex": "I am writing to inform you about the site status."},
        {"en": "Feel free to contact me", "fr": "N'hésitez pas à me contacter", "ex": "Feel free to contact me if you need help."},
        {"en": "Thank you for your cooperation", "fr": "Merci pour votre coopération", "ex": "We fixed the issue. Thank you for your cooperation."},
        {"en": "Regarding your request", "fr": "Concernant votre demande", "ex": "Regarding your request, here is the file."},
        {"en": "In response to your email", "fr": "En réponse à votre email", "ex": "In response to your email dated April 1st..."},
        {"en": "Sorry for the delay", "fr": "Désolé pour le retard", "ex": "Sorry for the delay in getting back to you."},
        {"en": "Please let me know", "fr": "S'il vous plaît faites-moi savoir", "ex": "Please let me know your thoughts."},
        {"en": "I am pleased to confirm", "fr": "J'ai le plaisir de confirmer", "ex": "I am pleased to confirm our meeting."},
        {"en": "It's my pleasure", "fr": "C'est un plaisir", "ex": "Thanks for the help! - It's my pleasure."},
        {"en": "I would appreciate it if...", "fr": "J'apprécierais que...", "ex": "I would appreciate it if you could call me."},
        {"en": "Just a quick reminder", "fr": "Juste un petit rappel", "ex": "Just a quick reminder about the report."},
        {"en": "Yours sincerely", "fr": "Sincèrement vôtre", "ex": "Yours sincerely, Rosly."},

        # --- PHRASES IDIOMATIQUES ---
        {"en": "Bite the bullet", "fr": "Prendre son courage à deux mains", "ex": "I have to bite the bullet and see the dentist."},
        {"en": "Out of the blue", "fr": "À l'improviste", "ex": "He called me out of the blue."},
        {"en": "Hit the sack", "fr": "Aller se coucher", "ex": "I'm tired, I'm going to hit the sack."},
        {"en": "It's not rocket science", "fr": "C'est pas sorcier", "ex": "Using this app is not rocket science."},
        {"en": "Break the ice", "fr": "Briser la glace", "ex": "He told a joke to break the ice."},
        {"en": "Cost an arm and a leg", "fr": "Coûter les yeux de la tête", "ex": "This car cost an arm and a leg."},
        {"en": "Kill two birds with one stone", "fr": "Faire d'une pierre deux coups", "ex": "I'll go to the bank and the store, killing two birds with one stone."},
        {"en": "Once in a blue moon", "fr": "Tous les 36 du mois", "ex": "I go to the cinema once in a blue moon."},
        {"en": "The best of both worlds", "fr": "Le meilleur des deux mondes", "ex": "Working from home gives me the best of both worlds."},
        {"en": "Spill
