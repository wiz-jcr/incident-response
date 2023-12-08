PLAYBOOK = {
    "malware": {
        "1":"",
        "2":'''  - Isolate affected systems from the network to prevent further lateral movement.<br>
 - Implement firewall rules and network segmentation to restrict communication.<br>
 - Apply access controls and group policies to limit user privileges and contain the malware.<br>
 - Utilize endpoint protection tools to quarantine infected files and terminate malicious processes.<br>
 - Communicate with relevant stakeholders about the containment measures taken.''',
        "3":'''vConduct a thorough analysis of affected systems to identify and remove all instances of the malware.<br>
 - Update antivirus signatures and endpoint protection definitions to recognize and eliminate the threat.<br>
 - Patch and update systems to address vulnerabilities exploited by the malware.<br>
 - Implement system hardening measures to prevent similar incidents in the future.<br>
 - Engage with threat intelligence sources to understand the malware's persistence mechanisms.''',
        "4":''' - Restore affected systems and services from clean backups to ensure a known good state.<br>
 - Monitor restored systems for any signs of re-infection or persistence.<br>
 - Conduct comprehensive testing to verify the integrity and security of restored systems.<br>
 - Gradually re-integrate systems into the production environment after thorough validation.<br>
 - Communicate with users and stakeholders regarding the completion of the recovery process.''',
        "5": ''' - Conduct a post-incident review to analyze the effectiveness of the incident response.<br>
 - Document key findings, challenges, and improvements for future incident prevention.<br>
 - Update incident response plans based on lessons learned from the malware incident.<br>
 - Provide training and awareness programs for employees to enhance their ability to recognize and report malware.<br>
 - Share insights with the cybersecurity community to contribute to collective knowledge and resilience.'''
    },
    "ddos": {
        "1": "",
        "2": ''' - Implement rate limiting and traffic filtering rules to mitigate the impact.<br>
 - Divert traffic through DDoS mitigation services to absorb and filter malicious traffic.<br>
 - Adjust firewall configurations to block or filter traffic from known malicious sources.<br>
 - Notify upstream ISPs to assist in blocking or mitigating the DDoS attack.''',
        "3": ''' - Collaborate with DDoS mitigation service providers to fine-tune filtering and blocking rules.<br>
 - Continuously monitor network traffic for signs of persistent or evolving DDoS attacks.<br>
 - Identify and address vulnerabilities that may have been exploited to facilitate the DDoS attack.<br>
 - Engage with law enforcement and threat intelligence sources to share attack details.''',
        "4": ''' - Gradually restore normal traffic as the DDoS attack is mitigated.<br>
 - Conduct post-incident analysis to understand the impact and improve future response.<br>
 - Implement additional DDoS prevention measures, such as network redundancy and load balancing.''',
        "5": ''' - Document the timeline and key observations during the DDoS incident.<br>
 - Assess the effectiveness of the response and identify areas for improvement.<br>
 - Share insights with industry peers and collaborate on collective DDoS defense strategies.<br>
 - Conduct training and simulations to enhance the team's readiness for future DDoS incidents.'''
    },
    "phishing": {
        "1": "",
        "2": ''' - Disable or block access to malicious URLs and domains identified in phishing emails.<br>
 - Quarantine or remove phishing emails from users' mailboxes.<br>
 - Communicate with affected users, advising them to change passwords and report any anomalies.<br>
 - Implement email filtering rules to block similar phishing emails across the organization.''',
        "3": ''' - Conduct forensic analysis to identify the source and methods used in the phishing campaign.<br>
 - Collaborate with law enforcement and threat intelligence sources to report and track phishing campaigns.<br>
 - Update email security configurations to enhance protection against future phishing attempts.<br>
 - Educate users on phishing prevention and response strategies.''',
        "4": ''' - Provide guidance to affected users on securing their accounts and devices.<br>
 - Conduct awareness training to educate employees on recognizing and reporting phishing attempts.<br>
 - Regularly update and reinforce email security policies and procedures.<br>
 - Monitor for any signs of account compromise or unauthorized access.''',
        "5": ''' - Analyze the effectiveness of phishing awareness training and user reporting mechanisms.<br>
 - Document the tactics and techniques used in the phishing campaign for future reference.<br>
 - Enhance incident response plans to include proactive measures for phishing prevention.<br>
 - Share threat intelligence with industry partners to collectively strengthen defenses against phishing.<br>
 - Conduct simulated phishing exercises to continually test and improve the organization's resilience to phishing attacks.'''
    }
}

system_prompt = '''You are an incident response specialist helping users, who do not have incident response team, to identify their incidents step by step. Your task is to instruct users to look for more details, especially signs of possible incidents. Once you are confident with the identified incident type, provide only one-sentence response beginning with "The incident is". Use a professional, conversational and empathic tone. Please provide response no more than 100 words.'''
