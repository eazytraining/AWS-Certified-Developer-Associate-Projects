#Lab: implementer AWS IAM Permission Boundaries

#Objectif
Apprenez à utiliser les limites de permission IAM pour limiter les permissions maximales qu'une entité IAM (utilisateur/rôle)
peut avoir, même si les politiques qui lui sont attachées lui accordent un accès plus large.



#Scénario d'Entreprise:Société Financière "SecureBank"

#Contexte:
L'équipe de développement de SecureBank doit déployer des applications critiques sur AWS, mais l'équipe de sécurité exige:
- Un accès lecture seule aux buckets S3 (contenant des données clients sensibles).
- Une interdiction de supprimer/modifier des ressources EC2 ou S3.
- Un mécanisme pour empêcher les développeurs de créer des rôles avec des privilèges excessifs.

#Problématique:

Les développeurs ont besoin de politiques IAM pour leurs tâches, mais pourraient accidentellement :
Attacher des politiques trop permissives (s3:*, ec2:*).
Créer des rôles avec des accès dangereux.

#Solution:

Utiliser des Permission Boundaries pour :
Limiter les développeurs à s3:Get*, s3:List*, ec2:Describe*.
Bloquer toute action d'écriture/suppression.

# Avantages pour SecureBank
- Sécurité: Prévention des erreurs coûteuses (ex: suppression accidentelle de données).
- Compliance: Respect des régulations financières (ex: RGPD).
- Délégation Sécurisée: Les développeurs peuvent créer des rôles sans risque de dérive de privilèges.

#Les etapes de realisation

#Prerequisites
- Un compte AWS avec un acces IAM.
- AWS CLI installe and configure (optionet, mais recommende pour la phase de teste).

Etape 1:creer la policy permission Boundary
- Créez une politique gérée qui agit comme le maximum d'autorisations autorisées (par exemple, l'accès en lecture seule à S3 et EC2).
- fichier json fournit pour se faire.

Etape 2:créer un utilisateur IAM avec des politiques trop permissives
 - Créez un utilisateur avec une politique qui accorde un accès complet à S3 et EC2, mais attachez la limite de permission pour la restreindre.
 - Fichier json founit a cet effet

Etape 3: teste des permissions
- Configurer les informations d'identification de l'utilisateur IAM dans AWS CLI
   aws configure --profile test-user
- Tester les actions autorisées (devrait réussir):
   # Lister les buckets S3 (permis par boundary)
   aws s3 ls --profile test-user
# Descrire les instances EC2 (permis par boundary)
   aws ec2 describe-instances --profile test-user
- Test Denied Actions (devrait échouer):
 # sayer de supprimer un bucket S3 (permis par boundary)
   aws s3 rb s3://your-bucket-name --force --profile test-user
# Essayer de resilier une instance EC2 (bloque par boundary)
   aws ec2 terminate-instances --instance-id i-1234567890 --profile test-user

# Comment ça marche?
Les autorisations effectives de l'utilisateur sont l'intersection des éléments suivants:
   - Les autorisations accordées par les politiques qui lui sont attachées (UserPolicy-FullS3EC2).
   - Les permissions autorisées par la frontière (Boundary-ReadOnlyS3EC2).
   - Même si l'utilisateur dispose de s3:*, la frontière le limite à s3:Get* et s3:List*.

Etape 4: cleanup
- Supprimer l'utilisateur IAM.
- Supprimer les politiques Boundary-ReadOnlyS3EC2 et UserPolicy-FullS3EC2.

