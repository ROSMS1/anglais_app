import streamlit as st
from gtts import gTTS
import os
import random

# ─────────────────────────────────────────────
# 1. PAGE CONFIGURATION
# ─────────────────────────────────────────────
st.set_page_config(page_title="SanaEnglishPro V3", page_icon="🎓", layout="wide")

# ─────────────────────────────────────────────
# 2. AUDIO FUNCTION
# ─────────────────────────────────────────────
def play_english(text, key_suffix=""):
    try:
        clean_text = text.split('(')[0].split('/')[0].split('—')[0].strip()
        tts = gTTS(text=clean_text, lang='en')
        filename = f"pronunciation_{key_suffix}.mp3"
        tts.save(filename)
        with open(filename, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")
        os.remove(filename)
    except Exception:
        st.error("Audio error. Please check your internet connection.")

# ─────────────────────────────────────────────
# 3. DATABASE (310+ EXPRESSIONS)
# ─────────────────────────────────────────────
ALL_DATA = {

    # ══════════════════════════════════════════
    # DAILY LIFE & GREETINGS
    # ══════════════════════════════════════════
    "Daily Life & Greetings": [
        {"en": "What's up?", "fr": "Quoi de neuf ?", "ex": "Hey man, what's up?"},
        {"en": "How's it going?", "fr": "Comment ça va ?", "ex": "How's it going with your new job?"},
        {"en": "Long time no see", "fr": "Ça fait un bail", "ex": "Oh, hi Mark! Long time no see."},
        {"en": "Take care", "fr": "Prends soin de toi", "ex": "See you tomorrow, take care!"},
        {"en": "Have a good one", "fr": "Bonne journée", "ex": "Thanks, you have a good one too."},
        {"en": "I'm exhausted", "fr": "Je suis épuisé", "ex": "I worked 10 hours, I'm exhausted."},
        {"en": "I'm starving", "fr": "Je meurs de faim", "ex": "Let's eat, I'm starving."},
        {"en": "It's up to you", "fr": "C'est toi qui décides", "ex": "Pizza or pasta? It's up to you."},
        {"en": "I don't mind", "fr": "Ça ne me dérange pas", "ex": "I don't mind waiting."},
        {"en": "Never mind", "fr": "Laisse tomber / C'est pas grave", "ex": "Never mind, I found my keys."},
        {"en": "No worries", "fr": "Pas de souci", "ex": "You're late? No worries."},
        {"en": "What do you mean?", "fr": "Que veux-tu dire ?", "ex": "I don't understand, what do you mean?"},
        {"en": "I guess so", "fr": "Je suppose que oui", "ex": "Is it going to rain? I guess so."},
        {"en": "Check this out", "fr": "Regarde ça", "ex": "Check this out, it's a new app."},
        {"en": "My bad", "fr": "C'est ma faute", "ex": "I forgot to call you, my bad."},
        {"en": "Anyway...", "fr": "Bref / De toute façon...", "ex": "Anyway, let's talk about something else."},
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
    ],

    # ══════════════════════════════════════════
    # WORK & MEETINGS
    # ══════════════════════════════════════════
    "Work & Meetings": [
        {"en": "Get down to business", "fr": "Passons aux choses sérieuses", "ex": "Let's get down to business."},
        {"en": "Keep me posted", "fr": "Tiens-moi au courant", "ex": "Keep me posted on the situation."},
        {"en": "In a nutshell", "fr": "En résumé", "ex": "In a nutshell, we are losing money."},
        {"en": "Think out of the box", "fr": "Penser différemment", "ex": "We need to think out of the box."},
        {"en": "Call it a day", "fr": "Finir sa journée", "ex": "It's 6 PM, let's call it a day."},
        {"en": "Work from home (WFH)", "fr": "Télétravail", "ex": "I work from home on Fridays."},
        {"en": "To be on the same page", "fr": "Être sur la même longueur d'onde", "ex": "We need to be on the same page."},
        {"en": "Back to square one", "fr": "Retour à la case départ", "ex": "The plan failed, back to square one."},
        {"en": "Win-win situation", "fr": "Situation gagnant-gagnant", "ex": "It's a win-win situation for us."},
        {"en": "Piece of cake", "fr": "C'est du gâteau / Très facile", "ex": "That exam was a piece of cake."},
        {"en": "The bottom line", "fr": "L'essentiel", "ex": "The bottom line is we need more users."},
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
        {"en": "Let's wrap it up", "fr": "Finissons-en", "ex": "It's late, let's wrap it up."},
        {"en": "What do you think?", "fr": "Qu'en penses-tu ?", "ex": "I like it, what do you think?"},
        {"en": "Any questions?", "fr": "Des questions ?", "ex": "That's all, any questions?"},
        {"en": "To postpone", "fr": "Reporter", "ex": "The meeting is postponed to Friday."},
        {"en": "Keep up the good work", "fr": "Continue ton bon travail", "ex": "Great results, keep up the good work!"},
        {"en": "I'm in charge of...", "fr": "Je suis responsable de...", "ex": "I'm in charge of maintenance."},
    ],

    # ══════════════════════════════════════════
    # TELECOM & NETWORK
    # ══════════════════════════════════════════
    "Telecom & Network": [
        {"en": "To troubleshoot", "fr": "Dépanner / Résoudre", "ex": "I need to troubleshoot this site."},
        {"en": "Site audit", "fr": "Audit de site", "ex": "We are conducting a site audit."},
        {"en": "Power failure", "fr": "Panne d'électricité", "ex": "There is a power failure at site X."},
        {"en": "Microwave link", "fr": "Lien hertzien", "ex": "The microwave link is down."},
        {"en": "To perform a test", "fr": "Effectuer un test", "ex": "Let's perform a loop test."},
        {"en": "To align antennas", "fr": "Aligner les antennes", "ex": "You need to align the antennas properly."},
        {"en": "Signal degradation", "fr": "Dégradation du signal", "ex": "We noticed signal degradation on the link."},
        {"en": "Outage", "fr": "Coupure / Panne totale", "ex": "We had a major outage last night."},
        {"en": "Root cause analysis (RCA)", "fr": "Analyse de la cause racine", "ex": "The RCA report is due by Monday."},
        {"en": "Mean Time To Repair (MTTR)", "fr": "Temps moyen de réparation", "ex": "We need to reduce our MTTR."},
        {"en": "Mean Time Between Failures (MTBF)", "fr": "Temps moyen entre pannes", "ex": "The MTBF for this battery is 5 years."},
        {"en": "Preventive maintenance", "fr": "Maintenance préventive", "ex": "Schedule preventive maintenance every quarter."},
        {"en": "Corrective maintenance", "fr": "Maintenance corrective", "ex": "The team is on-site for corrective maintenance."},
        {"en": "To escalate", "fr": "Escalader / Remonter", "ex": "Escalate this ticket to the back office."},
        {"en": "Ticket", "fr": "Bon de travail / Ticket", "ex": "Open a ticket for this fault."},
        {"en": "To restore service", "fr": "Rétablir le service", "ex": "We managed to restore service in 2 hours."},
        {"en": "Interference", "fr": "Interférence", "ex": "There is RF interference on this sector."},
        {"en": "Cell blocking", "fr": "Blocage de cellule", "ex": "Cell blocking rate is above threshold."},
        {"en": "Handover failure", "fr": "Échec de transfert intercellulaire", "ex": "Handover failure rate increased on site A."},
        {"en": "Network congestion", "fr": "Congestion réseau", "ex": "Network congestion during peak hours."},
        {"en": "Backhaul", "fr": "Réseau de transport/collecte", "ex": "The backhaul capacity needs upgrading."},
        {"en": "Fiber cut", "fr": "Coupure de fibre", "ex": "A fiber cut caused the outage."},
        {"en": "Rectifier", "fr": "Redresseur", "ex": "The rectifier module needs replacement."},
        {"en": "Battery bank", "fr": "Banque de batteries", "ex": "The battery bank autonomy is 4 hours."},
        {"en": "State of Health (SoH)", "fr": "État de santé (batterie)", "ex": "Check the SoH before deploying."},
        {"en": "Capacity planning", "fr": "Planification de la capacité", "ex": "Capacity planning is essential for growth."},
        {"en": "Field technician", "fr": "Technicien terrain", "ex": "Send the field technician immediately."},
        {"en": "Spare parts", "fr": "Pièces de rechange", "ex": "We are out of spare parts for this model."},
        {"en": "To swap", "fr": "Permuter / Remplacer", "ex": "Swap the faulty board with a new one."},
        {"en": "Commissioning", "fr": "Mise en service", "ex": "The commissioning of the new site is complete."},
        {"en": "Drive test", "fr": "Test de couverture terrain", "ex": "Perform a drive test after optimization."},
        {"en": "Coverage gap", "fr": "Zone de manque de couverture", "ex": "There is a coverage gap in the south zone."},
        {"en": "KPI (Key Performance Indicator)", "fr": "Indicateur de performance clé", "ex": "KPI degraded after the software update."},
        {"en": "To patch", "fr": "Appliquer un correctif", "ex": "Patch the software before the next audit."},
        {"en": "Configuration file", "fr": "Fichier de configuration", "ex": "Back up the configuration file first."},
        {"en": "Remote access", "fr": "Accès à distance", "ex": "I will troubleshoot via remote access."},
        {"en": "Alarm threshold", "fr": "Seuil d'alarme", "ex": "Set the alarm threshold to -75 dBm."},
        {"en": "On-site inspection", "fr": "Inspection sur site", "ex": "An on-site inspection is needed urgently."},
        {"en": "Power supply", "fr": "Alimentation électrique", "ex": "Check the power supply voltage."},
        {"en": "Earth fault", "fr": "Défaut de mise à la terre", "ex": "An earth fault was detected at the shelter."},
    ],

    # ══════════════════════════════════════════
    # EMAILS & PROFESSIONAL WRITING
    # ══════════════════════════════════════════
    "Emails & Writing": [
        {"en": "I hope this email finds you well", "fr": "J'espère que vous allez bien", "ex": "Dear Eric, I hope this email finds you well."},
        {"en": "Further to our conversation...", "fr": "Suite à notre conversation...", "ex": "Further to our conversation this morning..."},
        {"en": "Please find attached", "fr": "Veuillez trouver ci-joint", "ex": "Please find attached the report."},
        {"en": "Could you please clarify...?", "fr": "Pourriez-vous clarifier... ?", "ex": "Could you please clarify what you mean?"},
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
        {"en": "I would appreciate it if...", "fr": "J'apprécierais que...", "ex": "I would appreciate it if you could call me."},
        {"en": "Just a quick reminder", "fr": "Juste un petit rappel", "ex": "Just a quick reminder about the report."},
        {"en": "Yours sincerely", "fr": "Sincèrement vôtre", "ex": "Yours sincerely, Rosly."},
        {"en": "As per our agreement", "fr": "Comme convenu", "ex": "As per our agreement, I am sending the file."},
        {"en": "I would like to draw your attention to...", "fr": "Je voudrais attirer votre attention sur...", "ex": "I would like to draw your attention to the fault."},
        {"en": "Please be advised that...", "fr": "Veuillez noter que...", "ex": "Please be advised that the site is down."},
        {"en": "For your information (FYI)", "fr": "Pour information", "ex": "FYI, the audit is scheduled for Thursday."},
        {"en": "Action required", "fr": "Action requise", "ex": "Action required: sign the document today."},
        {"en": "Please revert by...", "fr": "Merci de répondre avant...", "ex": "Please revert by end of day Friday."},
    ],

    # ══════════════════════════════════════════
    # NEGOTIATION & FORMAL LANGUAGE
    # ══════════════════════════════════════════
    "Negotiation & Formal": [
        {"en": "I'd like to propose...", "fr": "Je voudrais proposer...", "ex": "I'd like to propose a new schedule."},
        {"en": "Could we find a middle ground?", "fr": "Pourrions-nous trouver un compromis ?", "ex": "Could we find a middle ground on the budget?"},
        {"en": "That's non-negotiable", "fr": "Ce n'est pas négociable", "ex": "The deadline is non-negotiable."},
        {"en": "I take your point, however...", "fr": "Je comprends votre point, cependant...", "ex": "I take your point, however the cost is too high."},
        {"en": "Let's agree to disagree", "fr": "Acceptons de ne pas être d'accord", "ex": "We see this differently, let's agree to disagree."},
        {"en": "We need to revisit this", "fr": "Nous devons revoir cela", "ex": "The numbers are wrong, we need to revisit this."},
        {"en": "That's within our scope", "fr": "Cela entre dans notre périmètre", "ex": "That work is within our scope of the contract."},
        {"en": "That's out of scope", "fr": "Ce n'est pas dans notre périmètre", "ex": "This request is out of scope for now."},
        {"en": "To sign off on", "fr": "Valider / Approuver formellement", "ex": "The manager needs to sign off on this."},
        {"en": "To put forward a proposal", "fr": "Soumettre une proposition", "ex": "We will put forward a proposal by Friday."},
        {"en": "Subject to approval", "fr": "Sous réserve d'approbation", "ex": "This is subject to approval from management."},
        {"en": "To raise a concern", "fr": "Soulever une préoccupation", "ex": "I'd like to raise a concern about safety."},
        {"en": "To reach a consensus", "fr": "Parvenir à un consensus", "ex": "The team reached a consensus on the plan."},
        {"en": "On behalf of...", "fr": "Au nom de...", "ex": "On behalf of MTN, I thank you."},
        {"en": "I stand corrected", "fr": "Je reconnais mon erreur", "ex": "You're right, I stand corrected."},
        {"en": "With all due respect...", "fr": "Avec tout le respect que je vous dois...", "ex": "With all due respect, I disagree."},
        {"en": "To clarify my position", "fr": "Pour clarifier ma position", "ex": "Let me clarify my position on this issue."},
        {"en": "Pending your confirmation", "fr": "En attente de votre confirmation", "ex": "We will proceed pending your confirmation."},
        {"en": "To iron out the details", "fr": "Régler les détails", "ex": "Let's iron out the details before signing."},
        {"en": "To table a motion", "fr": "Soumettre une motion", "ex": "She tabled a motion to extend the contract."},
    ],

    # ══════════════════════════════════════════
    # PHRASAL VERBS
    # ══════════════════════════════════════════
    "Phrasal Verbs": [
        {"en": "To back up", "fr": "Sauvegarder / Reculer / Soutenir", "ex": "Back up the data before the upgrade."},
        {"en": "To break down", "fr": "Tomber en panne / Décomposer", "ex": "The generator broke down last night."},
        {"en": "To bring up", "fr": "Mentionner / Soulever", "ex": "I need to bring up an issue in the meeting."},
        {"en": "To burn out", "fr": "S'épuiser / Griller (électrique)", "ex": "The fuse burned out during the storm."},
        {"en": "To carry out", "fr": "Effectuer / Réaliser", "ex": "Carry out the tests before sign-off."},
        {"en": "To check in", "fr": "S'enregistrer / Faire un point", "ex": "Let's check in after the maintenance."},
        {"en": "To come up with", "fr": "Trouver / Proposer", "ex": "We came up with a new solution."},
        {"en": "To cut off", "fr": "Couper / Interrompre", "ex": "The power was cut off for 3 hours."},
        {"en": "To deal with", "fr": "Traiter / S'occuper de", "ex": "I'll deal with this ticket now."},
        {"en": "To fall behind", "fr": "Prendre du retard", "ex": "We're falling behind on the project."},
        {"en": "To figure out", "fr": "Comprendre / Résoudre", "ex": "I need to figure out why the link is down."},
        {"en": "To fill in", "fr": "Remplir / Remplacer quelqu'un", "ex": "Fill in the checklist on site."},
        {"en": "To hand over", "fr": "Remettre / Transférer", "ex": "Hand over the site to the client today."},
        {"en": "To kick off", "fr": "Démarrer / Lancer", "ex": "The project kicks off on Monday."},
        {"en": "To lay out", "fr": "Présenter / Exposer", "ex": "Lay out the steps in the report."},
        {"en": "To look into", "fr": "Examiner / Investiguer", "ex": "I'll look into this issue."},
        {"en": "To phase out", "fr": "Éliminer progressivement", "ex": "Old batteries are being phased out."},
        {"en": "To point out", "fr": "Souligner / Indiquer", "ex": "I'd like to point out this error."},
        {"en": "To put off", "fr": "Reporter", "ex": "Don't put off the preventive maintenance."},
        {"en": "To run out of", "fr": "Manquer de / Être à court de", "ex": "We ran out of spare parts."},
        {"en": "To set up", "fr": "Installer / Configurer", "ex": "Set up the new equipment on the shelter."},
        {"en": "To shut down", "fr": "Éteindre / Arrêter", "ex": "Shut down the BTS before working on it."},
        {"en": "To sort out", "fr": "Résoudre / Régler", "ex": "I will sort out the configuration issue."},
        {"en": "To stand by", "fr": "Se tenir prêt / Attendre", "ex": "Stand by, we are resetting the equipment."},
        {"en": "To step up", "fr": "Intensifier / Prendre les choses en main", "ex": "We need to step up our maintenance efforts."},
        {"en": "To take over", "fr": "Reprendre / Prendre en charge", "ex": "I'll take over the ticket from here."},
        {"en": "To track down", "fr": "Retrouver / Localiser", "ex": "Track down the faulty module in the rack."},
        {"en": "To turn off", "fr": "Éteindre", "ex": "Turn off the alarm after fixing the fault."},
        {"en": "To wrap up", "fr": "Terminer / Conclure", "ex": "Let's wrap up the site visit report."},
        {"en": "To zoom in on", "fr": "Se concentrer sur", "ex": "Let's zoom in on the root cause."},
    ],

    # ══════════════════════════════════════════
    # IDIOMS
    # ══════════════════════════════════════════
    "Idioms": [
        {"en": "Bite the bullet", "fr": "Prendre son courage à deux mains", "ex": "I have to bite the bullet and see the dentist."},
        {"en": "Out of the blue", "fr": "À l'improviste", "ex": "He called me out of the blue."},
        {"en": "Hit the sack", "fr": "Aller se coucher", "ex": "I'm tired, I'm going to hit the sack."},
        {"en": "It's not rocket science", "fr": "C'est pas sorcier", "ex": "Using this app is not rocket science."},
        {"en": "Break the ice", "fr": "Briser la glace", "ex": "He told a joke to break the ice."},
        {"en": "Cost an arm and a leg", "fr": "Coûter les yeux de la tête", "ex": "This car cost an arm and a leg."},
        {"en": "Spill the beans", "fr": "Vendre la mèche", "ex": "Don't spill the beans about the party."},
        {"en": "Take it with a grain of salt", "fr": "Prendre avec des pincettes", "ex": "Take his advice with a grain of salt."},
        {"en": "Blessing in disguise", "fr": "Un mal pour un bien", "ex": "Losing that job was a blessing in disguise."},
        {"en": "Beat around the bush", "fr": "Tourner autour du pot", "ex": "Stop beating around the bush."},
        {"en": "Better late than never", "fr": "Mieux vaut tard que jamais", "ex": "You're late! - Better late than never."},
        {"en": "Cut somebody some slack", "fr": "Être indulgent", "ex": "He's new, cut him some slack."},
        {"en": "Get out of hand", "fr": "Dégénérer", "ex": "The party got out of hand."},
        {"en": "Hang in there", "fr": "Tiens bon", "ex": "I know it's hard, but hang in there."},
        {"en": "Hit the nail on the head", "fr": "Mettre le doigt sur le problème", "ex": "You hit the nail on the head."},
        {"en": "It's the last straw", "fr": "C'est la goutte d'eau", "ex": "He's late again! This is the last straw."},
        {"en": "Make a long story short", "fr": "Pour faire court", "ex": "To make a long story short, we won."},
        {"en": "No pain, no gain", "fr": "On n'a rien sans rien", "ex": "Keep training! No pain, no gain."},
        {"en": "Pull yourself together", "fr": "Reprends-toi", "ex": "Stop crying and pull yourself together."},
        {"en": "So far so good", "fr": "Jusqu'ici tout va bien", "ex": "The project is moving, so far so good."},
        {"en": "Through thick and thin", "fr": "Contre vents et marées", "ex": "They stayed together through thick and thin."},
        {"en": "Time flies", "fr": "Le temps passe vite", "ex": "Look at the time! Time flies."},
        {"en": "You can say that again", "fr": "Je suis tout à fait d'accord", "ex": "It's hot! - You can say that again."},
        {"en": "Your guess is as good as mine", "fr": "Je n'en sais pas plus que toi", "ex": "When will it start? - Your guess is as good as mine."},
        {"en": "Burn the midnight oil", "fr": "Travailler tard dans la nuit", "ex": "I burned the midnight oil to finish the report."},
        {"en": "The ball is in your court", "fr": "C'est à toi de jouer", "ex": "I sent the proposal, the ball is in your court."},
        {"en": "Bite off more than you can chew", "fr": "Avoir les yeux plus gros que le ventre", "ex": "Don't bite off more than you can chew."},
        {"en": "Go the extra mile", "fr": "Se surpasser / Faire plus que le minimum", "ex": "He always goes the extra mile for clients."},
        {"en": "The devil is in the details", "fr": "Les détails font toute la différence", "ex": "Check everything twice, the devil is in the details."},
        {"en": "A blessing in disguise", "fr": "Un bienfait caché", "ex": "That failure was a blessing in disguise."},
    ],

    # ══════════════════════════════════════════
    # IRREGULAR VERBS
    # ══════════════════════════════════════════
    "Irregular Verbs": [
        {"en": "To bear (bore/borne)", "fr": "Supporter", "ex": "I can't bear this noise."},
        {"en": "To beat (beat/beaten)", "fr": "Battre", "ex": "Our team beat theirs."},
        {"en": "To become (became/become)", "fr": "Devenir", "ex": "He became a doctor."},
        {"en": "To begin (began/begun)", "fr": "Commencer", "ex": "Let's begin the meeting."},
        {"en": "To bite (bit/bitten)", "fr": "Mordre", "ex": "The dog bit me."},
        {"en": "To blow (blew/blown)", "fr": "Souffler", "ex": "The wind blew hard."},
        {"en": "To break (broke/broken)", "fr": "Casser", "ex": "I broke my glasses."},
        {"en": "To bring (brought/brought)", "fr": "Apporter", "ex": "Bring me the report."},
        {"en": "To build (built/built)", "fr": "Construire", "ex": "They built a new site."},
        {"en": "To burn (burnt/burnt)", "fr": "Brûler", "ex": "The wires burnt out."},
        {"en": "To buy (bought/bought)", "fr": "Acheter", "ex": "I bought a new SFP module."},
        {"en": "To catch (caught/caught)", "fr": "Attraper", "ex": "Catch the ball!"},
        {"en": "To choose (chose/chosen)", "fr": "Choisir", "ex": "Choose a color."},
        {"en": "To cut (cut/cut)", "fr": "Couper", "ex": "Cut the power."},
        {"en": "To do (did/done)", "fr": "Faire", "ex": "I did my homework."},
        {"en": "To draw (drew/drawn)", "fr": "Dessiner", "ex": "Draw a diagram."},
        {"en": "To drive (drove/driven)", "fr": "Conduire", "ex": "I drive to the site."},
        {"en": "To fall (fell/fallen)", "fr": "Tomber", "ex": "The antenna fell."},
        {"en": "To feel (felt/felt)", "fr": "Ressentir", "ex": "I feel tired."},
        {"en": "To find (found/found)", "fr": "Trouver", "ex": "I found the fault."},
        {"en": "To forget (forgot/forgotten)", "fr": "Oublier", "ex": "Don't forget the keys."},
        {"en": "To get (got/got)", "fr": "Obtenir", "ex": "I got the message."},
        {"en": "To give (gave/given)", "fr": "Donner", "ex": "Give me a hand."},
        {"en": "To hear (heard/heard)", "fr": "Entendre", "ex": "Can you hear me?"},
        {"en": "To keep (kept/kept)", "fr": "Garder", "ex": "Keep the change."},
        {"en": "To know (knew/known)", "fr": "Savoir", "ex": "I know the answer."},
        {"en": "To lead (led/led)", "fr": "Mener / Diriger", "ex": "He leads the team."},
        {"en": "To learn (learnt/learnt)", "fr": "Apprendre", "ex": "I am learning English."},
        {"en": "To leave (left/left)", "fr": "Partir / Quitter", "ex": "I am leaving now."},
        {"en": "To lose (lost/lost)", "fr": "Perdre", "ex": "I lost my phone."},
        {"en": "To make (made/made)", "fr": "Faire / Fabriquer", "ex": "I made a mistake."},
        {"en": "To mean (meant/meant)", "fr": "Signifier", "ex": "What does it mean?"},
        {"en": "To meet (met/met)", "fr": "Rencontrer", "ex": "I met him at the conference."},
        {"en": "To run (ran/run)", "fr": "Courir / Faire tourner", "ex": "Run the diagnostic test."},
        {"en": "To send (sent/sent)", "fr": "Envoyer", "ex": "Send the file now."},
        {"en": "To speak (spoke/spoken)", "fr": "Parler", "ex": "I spoke to the engineer."},
        {"en": "To take (took/taken)", "fr": "Prendre", "ex": "Take a reading of the voltage."},
        {"en": "To tell (told/told)", "fr": "Dire / Raconter", "ex": "Tell me the fault details."},
        {"en": "To understand (understood/understood)", "fr": "Comprendre", "ex": "I understood the problem."},
        {"en": "To write (wrote/written)", "fr": "Écrire", "ex": "Write the RCA report."},
    ],

    # ══════════════════════════════════════════
    # MLK – KEY VOCABULARY (Level 2 Story)
    # ══════════════════════════════════════════
    "MLK – Key Vocabulary": [
        {"en": "Segregation", "fr": "Ségrégation raciale", "ex": "Segregation kept Black and white children in separate schools."},
        {"en": "Equality", "fr": "Égalité", "ex": "Martin Luther King fought for equality for all people."},
        {"en": "Racism", "fr": "Racisme", "ex": "He spoke out against racism his whole life."},
        {"en": "Non-violence", "fr": "Non-violence", "ex": "Gandhi and King both believed in non-violence."},
        {"en": "Protest", "fr": "Manifestation / Protestation", "ex": "They organised a peaceful protest in the city centre."},
        {"en": "Boycott", "fr": "Boycott", "ex": "The Montgomery Bus Boycott lasted 381 days."},
        {"en": "Civil rights", "fr": "Droits civiques", "ex": "The Civil Rights Act of 1964 banned segregation in public places."},
        {"en": "Legacy", "fr": "Héritage / Legs", "ex": "His legacy continues to inspire people around the world."},
        {"en": "Justice", "fr": "Justice", "ex": "He dedicated his life to the pursuit of justice."},
        {"en": "Dignity", "fr": "Dignité", "ex": "Every human being deserves to be treated with dignity."},
        {"en": "Injustice", "fr": "Injustice", "ex": "They marched to protest the injustice in their country."},
        {"en": "Discrimination", "fr": "Discrimination", "ex": "Racial discrimination was written into law in many states."},
        {"en": "Assassination", "fr": "Assassinat", "ex": "His assassination in 1968 shocked the entire world."},
        {"en": "Movement", "fr": "Mouvement (social)", "ex": "He was the leader of the Civil Rights Movement."},
        {"en": "March", "fr": "Marche (protestataire)", "ex": "Over 250,000 people joined the March on Washington."},
        {"en": "Minister / Preacher", "fr": "Pasteur / Prédicateur", "ex": "Martin became a Baptist minister like his father."},
        {"en": "Strike", "fr": "Grève", "ex": "He went to Memphis to support workers who were on strike."},
        {"en": "Supreme Court", "fr": "Cour Suprême", "ex": "The Supreme Court ruled that bus segregation was illegal."},
        {"en": "Nobel Peace Prize", "fr": "Prix Nobel de la Paix", "ex": "Martin Luther King won the Nobel Peace Prize in 1964."},
        {"en": "Volunteer work", "fr": "Travail bénévole", "ex": "On MLK Day, Americans do volunteer work in their communities."},
        {"en": "Water fountain", "fr": "Fontaine à eau / Robinet public", "ex": "Black people had to use separate water fountains."},
        {"en": "Unfair", "fr": "Injuste", "ex": "Even as a child, Martin saw that the system was unfair."},
        {"en": "Courage", "fr": "Courage", "ex": "Rosa Parks showed incredible courage by refusing to give up her seat."},
        {"en": "Freedom", "fr": "Liberté", "ex": "He dreamed of a nation where all people would live in freedom."},
        {"en": "Unity", "fr": "Unité", "ex": "His speech was a call for unity between all races."},
        {"en": "To gather", "fr": "Se rassembler", "ex": "Thousands gathered at the Lincoln Memorial."},
        {"en": "To be arrested", "fr": "Être arrêté", "ex": "He was arrested many times during the movement."},
        {"en": "To give up (one's seat)", "fr": "Céder (sa place)", "ex": "Rosa Parks refused to give up her seat on the bus."},
        {"en": "To be judged by", "fr": "Être jugé par / selon", "ex": "He dreamed that people would be judged by their character, not their skin."},
        {"en": "To change the law", "fr": "Changer la loi", "ex": "Their peaceful protests helped change the laws of the country."},
    ],

    # ══════════════════════════════════════════
    # MLK – POWER EXPRESSIONS (Full Story)
    # ══════════════════════════════════════════
    "MLK – Power Expressions": [
        {"en": "To stand up for", "fr": "Se battre pour / Défendre", "ex": "You must stand up for what you believe in."},
        {"en": "To speak out against", "fr": "S'élever contre / Dénoncer", "ex": "He spent his life speaking out against racism."},
        {"en": "To keep moving forward", "fr": "Continuer d'avancer", "ex": "Despite all the threats, he kept moving forward."},
        {"en": "To meet hate with love", "fr": "Répondre à la haine par l'amour", "ex": "Martin always said: we must meet hate with love."},
        {"en": "To make a statement", "fr": "Envoyer un message fort / Faire une déclaration", "ex": "By walking instead of riding, they were making a statement."},
        {"en": "To put down (weapons)", "fr": "Déposer (les armes)", "ex": "The crowd put down their weapons when Martin spoke."},
        {"en": "To stand strong", "fr": "Tenir bon / Rester debout", "ex": "Even under pressure, they stood strong together."},
        {"en": "To be drawn to someone", "fr": "Être attiré par quelqu'un", "ex": "He was drawn to her because of her mind and her heart."},
        {"en": "To be in need", "fr": "Être dans le besoin", "ex": "He helped people who were in need."},
        {"en": "To echo through time", "fr": "Résonner à travers le temps", "ex": "His words still echo through time today."},
        {"en": "To open someone's eyes", "fr": "Ouvrir les yeux de quelqu'un", "ex": "The images of children being attacked opened the world's eyes."},
        {"en": "To light a fire in someone's heart", "fr": "Allumer un feu dans le cœur de quelqu'un", "ex": "That moment lit a fire in Martin's heart."},
        {"en": "To hold people together", "fr": "Maintenir les gens unis", "ex": "A great leader knows how to hold people together in hard times."},
        {"en": "To make up one's mind", "fr": "Prendre sa décision / Se décider", "ex": "By the end of college, Martin had made up his mind to become a minister."},
        {"en": "To have a deep urge to", "fr": "Ressentir une forte envie de", "ex": "He wrote: I have a deep urge to serve humanity."},
        {"en": "Second-class citizens", "fr": "Citoyens de seconde zone", "ex": "They were tired of being treated like second-class citizens."},
        {"en": "To be humiliated", "fr": "Être humilié", "ex": "They were humiliated every single day by the system."},
        {"en": "To tap someone's phone", "fr": "Mettre quelqu'un sur écoute", "ex": "The FBI tapped his phone to spy on him."},
        {"en": "Miraculously", "fr": "Miraculeusement", "ex": "Miraculously, his wife and baby survived the bomb."},
        {"en": "To shatter", "fr": "Briser / Fracasser", "ex": "The blast shattered every window in the house."},
        {"en": "To be a bridge between", "fr": "Être un pont entre", "ex": "He wanted to be a bridge between pain and peace."},
        {"en": "A spark", "fr": "Une étincelle", "ex": "Rosa Parks' small act of courage became a spark for the whole movement."},
        {"en": "Destiny is calling", "fr": "Le destin vous appelle", "ex": "He didn't plan to be a leader, but destiny was calling."},
        {"en": "To lose courage", "fr": "Perdre courage", "ex": "Late at night, alone in his kitchen, he felt he was losing courage."},
        {"en": "At the end of one's powers", "fr": "À bout de forces", "ex": "He whispered: I'm at the end of my powers."},
        {"en": "To be a target", "fr": "Être une cible", "ex": "His children grew up knowing their father was both a hero and a target."},
        {"en": "To be drawn into a story", "fr": "Être plongé dans une histoire", "ex": "Sit back and let the story take you in."},
        {"en": "To remain calm", "fr": "Rester calme", "ex": "Even with constant threats, Martin remained calm."},
        {"en": "To preach", "fr": "Prêcher / Donner un sermon", "ex": "His father preached at Ebenezer Baptist Church every Sunday."},
        {"en": "To be inspired by", "fr": "Être inspiré par", "ex": "Martin was deeply inspired by the ideas of Mahatma Gandhi."},
    ],
}

# ─────────────────────────────────────────────
# 4. SESSION STATE INITIALIZATION
# ─────────────────────────────────────────────
if 'favorites' not in st.session_state:
    st.session_state.favorites = []
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_total' not in st.session_state:
    st.session_state.quiz_total = 0
if 'quiz_state' not in st.session_state:
    st.session_state.quiz_state = None
if 'current_card' not in st.session_state:
    st.session_state.current_card = None
    st.session_state.current_cat = None
    st.session_state.show_ans = False

def get_all_items():
    items = []
    for cat, lst in ALL_DATA.items():
        for item in lst:
            items.append({**item, "cat": cat})
    return items

ALL_ITEMS = get_all_items()
TOTAL = len(ALL_ITEMS)

# ─────────────────────────────────────────────
# 5. MAIN INTERFACE
# ─────────────────────────────────────────────
st.title("🎓 SanaEnglishPro V3")
st.sidebar.title("📚 Navigation")
st.sidebar.metric("📦 Total expressions", TOTAL)
st.sidebar.metric("⭐ Favorites", len(st.session_state.favorites))
st.sidebar.metric(
    "🎯 Quiz Score",
    f"{st.session_state.quiz_score}/{st.session_state.quiz_total}" if st.session_state.quiz_total > 0 else "—"
)

menu = st.sidebar.selectbox(
    "Go to",
    ["🃏 Flashcards", "📚 Dictionary", "🎯 Quiz", "⭐ Favorites", "📊 Statistics"]
)

# ─────────────────────────────────────────────
# 6. FLASHCARDS
# ─────────────────────────────────────────────
if menu == "🃏 Flashcards":
    st.subheader("🃏 Random Training")

    selected_cat = st.selectbox("Select a category", ["🔀 Mix all"] + list(ALL_DATA.keys()))

    if selected_cat == "🔀 Mix all":
        pool = ALL_ITEMS
    else:
        pool = [{**item, "cat": selected_cat} for item in ALL_DATA[selected_cat]]

    if st.session_state.current_card is None or st.session_state.current_cat != selected_cat:
        st.session_state.current_card = random.choice(pool)
        st.session_state.current_cat = selected_cat
        st.session_state.show_ans = False

    card = st.session_state.current_card

    st.caption(f"📂 Category: **{card.get('cat', selected_cat)}**")

    st.markdown(f"""
    <div style="background: linear-gradient(135deg,#1a1a2e,#16213e);
                border-radius:16px; padding:32px; text-align:center;
                border:2px solid #0f3460; margin-bottom:12px;">
        <p style="color:#a0aec0; font-size:14px; margin:0 0 8px 0;">🇬🇧 English expression</p>
        <h2 style="color:#e2e8f0; font-size:28px; margin:0;">{card['en']}</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🔊 Listen", use_container_width=True):
            play_english(card['en'], "flash")
    with col2:
        if st.button("🔄 Translate", use_container_width=True):
            st.session_state.show_ans = True
    with col3:
        if st.button("➡️ Next", use_container_width=True):
            st.session_state.current_card = random.choice(pool)
            st.session_state.show_ans = False
            st.rerun()
    with col4:
        is_fav = card['en'] in [f['en'] for f in st.session_state.favorites]
        fav_label = "💛 Remove" if is_fav else "⭐ Save"
        if st.button(fav_label, use_container_width=True):
            if is_fav:
                st.session_state.favorites = [f for f in st.session_state.favorites if f['en'] != card['en']]
                st.toast("Removed from favorites")
            else:
                st.session_state.favorites.append(card)
                st.toast("Added to favorites!")
            st.rerun()

    if st.session_state.show_ans:
        st.success(f"🇫🇷 **French:** {card['fr']}")
        st.info(f"💡 **Example:** *{card['ex']}*")

# ─────────────────────────────────────────────
# 7. DICTIONARY
# ─────────────────────────────────────────────
elif menu == "📚 Dictionary":
    st.subheader("📚 Full Expression Library")

    col_s, col_c = st.columns([2, 1])
    with col_s:
        search = st.text_input("🔍 Search an expression...", placeholder="e.g. outage, troubleshoot, deadline...")
    with col_c:
        cat_filter = st.selectbox("📂 Filter by category", ["All"] + list(ALL_DATA.keys()))

    if cat_filter == "All":
        pool = ALL_ITEMS
    else:
        pool = [{**item, "cat": cat_filter} for item in ALL_DATA[cat_filter]]

    if search:
        results = [i for i in pool if search.lower() in i['en'].lower() or search.lower() in i['fr'].lower()]
    else:
        results = pool

    st.caption(f"📊 Showing {len(results)} expression(s) out of {TOTAL}")

    for i, r in enumerate(results):
        with st.expander(f"🇬🇧 {r['en']}  ·  📂 {r.get('cat', '')}"):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.write(f"**🇫🇷 French:** {r['fr']}")
                st.write(f"**💡 Example:** *{r['ex']}*")
            with c2:
                if st.button("🔊", key=f"dict_audio_{i}", help="Pronounce"):
                    play_english(r['en'], f"dict_{i}")
                is_fav = r['en'] in [f['en'] for f in st.session_state.favorites]
                if st.button("💛" if is_fav else "⭐", key=f"dict_fav_{i}", help="Favorite"):
                    if is_fav:
                        st.session_state.favorites = [f for f in st.session_state.favorites if f['en'] != r['en']]
                    else:
                        st.session_state.favorites.append(r)
                    st.rerun()

# ─────────────────────────────────────────────
# 8. QUIZ
# ─────────────────────────────────────────────
elif menu == "🎯 Quiz":
    st.subheader("🎯 Multiple Choice Quiz")

    cat_q = st.selectbox("Select a category", ["🔀 Mix all"] + list(ALL_DATA.keys()), key="quiz_cat")

    if cat_q == "🔀 Mix all":
        pool = ALL_ITEMS
    else:
        pool = [{**item, "cat": cat_q} for item in ALL_DATA[cat_q]]

    def generate_quiz(pool):
        if len(pool) < 4:
            return None
        correct = random.choice(pool)
        wrong_pool = [x for x in pool if x['en'] != correct['en']]
        wrongs = random.sample(wrong_pool, min(3, len(wrong_pool)))
        choices = [correct['fr']] + [w['fr'] for w in wrongs]
        random.shuffle(choices)
        return {
            "question": correct['en'],
            "example": correct['ex'],
            "correct": correct['fr'],
            "choices": choices,
            "answered": None,
        }

    if st.button("🆕 New question", use_container_width=True) or st.session_state.quiz_state is None:
        st.session_state.quiz_state = generate_quiz(pool)

    q = st.session_state.quiz_state
    if q:
        st.markdown(f"""
        <div style="background:#1a1a2e; border-radius:12px; padding:24px;
                    border:2px solid #0f3460; margin-bottom:16px; text-align:center;">
            <p style="color:#a0aec0; margin:0 0 8px 0;">What is the French meaning of:</p>
            <h3 style="color:#63b3ed; margin:0;">{q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)

        if q['answered'] is None:
            for choice in q['choices']:
                if st.button(choice, key=f"choice_{choice}", use_container_width=True):
                    q['answered'] = choice
                    st.session_state.quiz_total += 1
                    if choice == q['correct']:
                        st.session_state.quiz_score += 1
                    st.rerun()
        else:
            for choice in q['choices']:
                if choice == q['correct']:
                    st.success(f"✅ {choice}")
                elif choice == q['answered'] and q['answered'] != q['correct']:
                    st.error(f"❌ {choice}")
                else:
                    st.button(choice, disabled=True, key=f"dis_{choice}")

            if q['answered'] == q['correct']:
                st.balloons()
                st.success("🎉 Correct answer!")
            else:
                st.error(f"The correct answer was: **{q['correct']}**")

            st.info(f"💡 Example: *{q['example']}*")

            pct = int((st.session_state.quiz_score / st.session_state.quiz_total) * 100) if st.session_state.quiz_total > 0 else 0
            st.metric("Current score", f"{st.session_state.quiz_score}/{st.session_state.quiz_total}", f"{pct}%")

            if st.button("➡️ Next question", use_container_width=True):
                st.session_state.quiz_state = generate_quiz(pool)
                st.rerun()

    if st.button("🔄 Reset score"):
        st.session_state.quiz_score = 0
        st.session_state.quiz_total = 0
        st.session_state.quiz_state = None
        st.rerun()

# ─────────────────────────────────────────────
# 9. FAVORITES
# ─────────────────────────────────────────────
elif menu == "⭐ Favorites":
    st.subheader("⭐ My Saved Expressions")

    if not st.session_state.favorites:
        st.info("No favorites yet. Tap ⭐ in Flashcards or Dictionary to save expressions.")
    else:
        st.caption(f"{len(st.session_state.favorites)} expression(s) saved")

        if st.button("🃏 Review my favorites (random)"):
            st.session_state.current_card = random.choice(st.session_state.favorites)
            st.session_state.current_cat = "Favorites"
            st.session_state.show_ans = False
            st.session_state.quiz_state = None

        for i, fav in enumerate(st.session_state.favorites):
            with st.expander(f"⭐ {fav['en']}  ·  📂 {fav.get('cat', '')}"):
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.write(f"**🇫🇷 French:** {fav['fr']}")
                    st.write(f"**💡 Example:** *{fav['ex']}*")
                with c2:
                    if st.button("🔊", key=f"fav_audio_{i}"):
                        play_english(fav['en'], f"fav_{i}")
                    if st.button("🗑️", key=f"fav_del_{i}", help="Remove"):
                        st.session_state.favorites.pop(i)
                        st.rerun()

# ─────────────────────────────────────────────
# 10. STATISTICS
# ─────────────────────────────────────────────
elif menu == "📊 Statistics":
    st.subheader("📊 Statistics & Goals")

    st.success(f"🎉 Database: **{TOTAL} expressions** across {len(ALL_DATA)} categories")

    st.write("### 📂 Breakdown by category")
    for cat, items in ALL_DATA.items():
        col_label, col_bar = st.columns([1, 3])
        with col_label:
            st.write(f"**{cat}**")
        with col_bar:
            st.progress(min(len(items) / 50, 1.0))
            st.caption(f"{len(items)} expressions")

    st.divider()

    st.write("### 🎯 Overall Quiz Score")
    if st.session_state.quiz_total > 0:
        pct = int(st.session_state.quiz_score / st.session_state.quiz_total * 100)
        st.metric("Correct answers", f"{st.session_state.quiz_score}/{st.session_state.quiz_total}", f"{pct}%")
        st.progress(pct / 100)
    else:
        st.info("Start a Quiz to see your score here.")

    st.divider()

    st.write("### 🚀 Tips for Rosly")
    tips = [
        ("🛠️", "**Telecom:** Browse the *Telecom & Network* category before writing incident reports."),
        ("📞", "**Listening:** Always play the audio before calls with Eric or the Back Office team."),
        ("🎯", "**Quiz:** 5 questions a day in *Negotiation & Formal* to sharpen your formal English."),
        ("⭐", "**Favorites:** Pin expressions you keep forgetting for focused review."),
        ("📧", "**Emails:** Open *Emails & Writing* before sending an RCA or formal report in English."),
        ("🔄", "**Phrasal Verbs:** These are the most used in spoken English — practice them every morning."),
    ]
    for icon, tip in tips:
        st.write(f"{icon} {tip}")

    st.balloons()
