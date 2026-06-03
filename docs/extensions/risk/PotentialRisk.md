---
search:
  boost: 10.0
---

# Class: PotentialRisk 


_Indicates a concept can potentially be a 'risk' concept within an_

_use-case_



<div data-search-exclude markdown="1">



URI: [risk:PotentialRisk](https://w3id.org/lmodel/dpv/risk/PotentialRisk)





```mermaid
 classDiagram
    class PotentialRisk
    click PotentialRisk href "../PotentialRisk/"
      PotentialRisk <|-- AccidentalMisuse
        click AccidentalMisuse href "../AccidentalMisuse/"
      PotentialRisk <|-- AccuracyDegraded
        click AccuracyDegraded href "../AccuracyDegraded/"
      PotentialRisk <|-- AccuracyInconsistent
        click AccuracyInconsistent href "../AccuracyInconsistent/"
      PotentialRisk <|-- AccuracyInsufficient
        click AccuracyInsufficient href "../AccuracyInsufficient/"
      PotentialRisk <|-- AccuracyRisk
        click AccuracyRisk href "../AccuracyRisk/"
      PotentialRisk <|-- AccuracyUnknown
        click AccuracyUnknown href "../AccuracyUnknown/"
      PotentialRisk <|-- AccuracyUnverified
        click AccuracyUnverified href "../AccuracyUnverified/"
      PotentialRisk <|-- AgeDiscrimination
        click AgeDiscrimination href "../AgeDiscrimination/"
      PotentialRisk <|-- AuthorisationFailure
        click AuthorisationFailure href "../AuthorisationFailure/"
      PotentialRisk <|-- AvailabilityBreach
        click AvailabilityBreach href "../AvailabilityBreach/"
      PotentialRisk <|-- BehaviourDistortion
        click BehaviourDistortion href "../BehaviourDistortion/"
      PotentialRisk <|-- BelievesDiscrimination
        click BelievesDiscrimination href "../BelievesDiscrimination/"
      PotentialRisk <|-- Benefit
        click Benefit href "../Benefit/"
      PotentialRisk <|-- Bias
        click Bias href "../Bias/"
      PotentialRisk <|-- Blackmail
        click Blackmail href "../Blackmail/"
      PotentialRisk <|-- BruteForceAuthorisations
        click BruteForceAuthorisations href "../BruteForceAuthorisations/"
      PotentialRisk <|-- CasteDiscrimination
        click CasteDiscrimination href "../CasteDiscrimination/"
      PotentialRisk <|-- Coercion
        click Coercion href "../Coercion/"
      PotentialRisk <|-- CognitiveBias
        click CognitiveBias href "../CognitiveBias/"
      PotentialRisk <|-- Compensation
        click Compensation href "../Compensation/"
      PotentialRisk <|-- ComponentFailure
        click ComponentFailure href "../ComponentFailure/"
      PotentialRisk <|-- ComponentMalfunction
        click ComponentMalfunction href "../ComponentMalfunction/"
      PotentialRisk <|-- CompromiseAccount
        click CompromiseAccount href "../CompromiseAccount/"
      PotentialRisk <|-- CompromiseAccountCredentials
        click CompromiseAccountCredentials href "../CompromiseAccountCredentials/"
      PotentialRisk <|-- ConfidentialityBreach
        click ConfidentialityBreach href "../ConfidentialityBreach/"
      PotentialRisk <|-- ConfirmationBias
        click ConfirmationBias href "../ConfirmationBias/"
      PotentialRisk <|-- ConfoundingVariablesBias
        click ConfoundingVariablesBias href "../ConfoundingVariablesBias/"
      PotentialRisk <|-- CopyrightViolation
        click CopyrightViolation href "../CopyrightViolation/"
      PotentialRisk <|-- CoverageBias
        click CoverageBias href "../CoverageBias/"
      PotentialRisk <|-- CredibilityLoss
        click CredibilityLoss href "../CredibilityLoss/"
      PotentialRisk <|-- Cryptojacking
        click Cryptojacking href "../Cryptojacking/"
      PotentialRisk <|-- CustomerConfidenceLoss
        click CustomerConfidenceLoss href "../CustomerConfidenceLoss/"
      PotentialRisk <|-- CustomerSupportLimited
        click CustomerSupportLimited href "../CustomerSupportLimited/"
      PotentialRisk <|-- Damage
        click Damage href "../Damage/"
      PotentialRisk <|-- DataAggregationBias
        click DataAggregationBias href "../DataAggregationBias/"
      PotentialRisk <|-- DataBias
        click DataBias href "../DataBias/"
      PotentialRisk <|-- DataBreach
        click DataBreach href "../DataBreach/"
      PotentialRisk <|-- DataCollectionError
        click DataCollectionError href "../DataCollectionError/"
      PotentialRisk <|-- DataCorruption
        click DataCorruption href "../DataCorruption/"
      PotentialRisk <|-- DataErasureError
        click DataErasureError href "../DataErasureError/"
      PotentialRisk <|-- DataInaccurate
        click DataInaccurate href "../DataInaccurate/"
      PotentialRisk <|-- DataIncomplete
        click DataIncomplete href "../DataIncomplete/"
      PotentialRisk <|-- DataInconsistent
        click DataInconsistent href "../DataInconsistent/"
      PotentialRisk <|-- DataLoss
        click DataLoss href "../DataLoss/"
      PotentialRisk <|-- DataMisclassified
        click DataMisclassified href "../DataMisclassified/"
      PotentialRisk <|-- DataMisinterpretation
        click DataMisinterpretation href "../DataMisinterpretation/"
      PotentialRisk <|-- DataNoise
        click DataNoise href "../DataNoise/"
      PotentialRisk <|-- DataOutdated
        click DataOutdated href "../DataOutdated/"
      PotentialRisk <|-- DataPreparationError
        click DataPreparationError href "../DataPreparationError/"
      PotentialRisk <|-- DataProcessingBias
        click DataProcessingBias href "../DataProcessingBias/"
      PotentialRisk <|-- DataProcessingError
        click DataProcessingError href "../DataProcessingError/"
      PotentialRisk <|-- DataRisk
        click DataRisk href "../DataRisk/"
      PotentialRisk <|-- DataSelectionError
        click DataSelectionError href "../DataSelectionError/"
      PotentialRisk <|-- DataSparse
        click DataSparse href "../DataSparse/"
      PotentialRisk <|-- DataStorageError
        click DataStorageError href "../DataStorageError/"
      PotentialRisk <|-- DataTransferError
        click DataTransferError href "../DataTransferError/"
      PotentialRisk <|-- DataUnavailable
        click DataUnavailable href "../DataUnavailable/"
      PotentialRisk <|-- DataUnrepresentative
        click DataUnrepresentative href "../DataUnrepresentative/"
      PotentialRisk <|-- DataUnstructured
        click DataUnstructured href "../DataUnstructured/"
      PotentialRisk <|-- DataUnverified
        click DataUnverified href "../DataUnverified/"
      PotentialRisk <|-- Deception
        click Deception href "../Deception/"
      PotentialRisk <|-- DelayedApplicationProcessing
        click DelayedApplicationProcessing href "../DelayedApplicationProcessing/"
      PotentialRisk <|-- DenialServiceAttack
        click DenialServiceAttack href "../DenialServiceAttack/"
      PotentialRisk <|-- Detriment
        click Detriment href "../Detriment/"
      PotentialRisk <|-- DirectDiscrimination
        click DirectDiscrimination href "../DirectDiscrimination/"
      PotentialRisk <|-- DisabilityDiscrimination
        click DisabilityDiscrimination href "../DisabilityDiscrimination/"
      PotentialRisk <|-- Discrimination
        click Discrimination href "../Discrimination/"
      PotentialRisk <|-- DisproportionateEnergyConsumption
        click DisproportionateEnergyConsumption href "../DisproportionateEnergyConsumption/"
      PotentialRisk <|-- DistributedDenialServiceAttack
        click DistributedDenialServiceAttack href "../DistributedDenialServiceAttack/"
      PotentialRisk <|-- DocumentationIssues
        click DocumentationIssues href "../DocumentationIssues/"
      PotentialRisk <|-- Earthquake
        click Earthquake href "../Earthquake/"
      PotentialRisk <|-- EnvironmentalRisk
        click EnvironmentalRisk href "../EnvironmentalRisk/"
      PotentialRisk <|-- EquipmentFailure
        click EquipmentFailure href "../EquipmentFailure/"
      PotentialRisk <|-- EquipmentMalfunction
        click EquipmentMalfunction href "../EquipmentMalfunction/"
      PotentialRisk <|-- ErroneousUse
        click ErroneousUse href "../ErroneousUse/"
      PotentialRisk <|-- EthnicDiscrimination
        click EthnicDiscrimination href "../EthnicDiscrimination/"
      PotentialRisk <|-- ExcellenceDiscrimination
        click ExcellenceDiscrimination href "../ExcellenceDiscrimination/"
      PotentialRisk <|-- Exploitation
        click Exploitation href "../Exploitation/"
      PotentialRisk <|-- ExposureToHarmfulSpeech
        click ExposureToHarmfulSpeech href "../ExposureToHarmfulSpeech/"
      PotentialRisk <|-- ExternalSecurityThreat
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      PotentialRisk <|-- Extortion
        click Extortion href "../Extortion/"
      PotentialRisk <|-- FinancialImpact
        click FinancialImpact href "../FinancialImpact/"
      PotentialRisk <|-- FinancialLoss
        click FinancialLoss href "../FinancialLoss/"
      PotentialRisk <|-- Floods
        click Floods href "../Floods/"
      PotentialRisk <|-- Fraud
        click Fraud href "../Fraud/"
      PotentialRisk <|-- GenderDiscrimination
        click GenderDiscrimination href "../GenderDiscrimination/"
      PotentialRisk <|-- GeographicDiscrimination
        click GeographicDiscrimination href "../GeographicDiscrimination/"
      PotentialRisk <|-- GoodwillLoss
        click GoodwillLoss href "../GoodwillLoss/"
      PotentialRisk <|-- GroupAttributionBias
        click GroupAttributionBias href "../GroupAttributionBias/"
      PotentialRisk <|-- GroupHealthSafety
        click GroupHealthSafety href "../GroupHealthSafety/"
      PotentialRisk <|-- GroupRisk
        click GroupRisk href "../GroupRisk/"
      PotentialRisk <|-- Harassment
        click Harassment href "../Harassment/"
      PotentialRisk <|-- Harm
        click Harm href "../Harm/"
      PotentialRisk <|-- Health
        click Health href "../Health/"
      PotentialRisk <|-- HealthSafety
        click HealthSafety href "../HealthSafety/"
      PotentialRisk <|-- Homophobia
        click Homophobia href "../Homophobia/"
      PotentialRisk <|-- HumanErrors
        click HumanErrors href "../HumanErrors/"
      PotentialRisk <|-- HumanOversightIneffective
        click HumanOversightIneffective href "../HumanOversightIneffective/"
      PotentialRisk <|-- HumanOversightInsufficient
        click HumanOversightInsufficient href "../HumanOversightInsufficient/"
      PotentialRisk <|-- IdentityFraud
        click IdentityFraud href "../IdentityFraud/"
      PotentialRisk <|-- IdentityTheft
        click IdentityTheft href "../IdentityTheft/"
      PotentialRisk <|-- IdentityVerificationFailure
        click IdentityVerificationFailure href "../IdentityVerificationFailure/"
      PotentialRisk <|-- IllegalDataProcessing
        click IllegalDataProcessing href "../IllegalDataProcessing/"
      PotentialRisk <|-- ImpairedDecisionMaking
        click ImpairedDecisionMaking href "../ImpairedDecisionMaking/"
      PotentialRisk <|-- ImplicitBias
        click ImplicitBias href "../ImplicitBias/"
      PotentialRisk <|-- InGroupBias
        click InGroupBias href "../InGroupBias/"
      PotentialRisk <|-- InabilityToEnterIntoContract
        click InabilityToEnterIntoContract href "../InabilityToEnterIntoContract/"
      PotentialRisk <|-- InabilityToEstablishLegalClaims
        click InabilityToEstablishLegalClaims href "../InabilityToEstablishLegalClaims/"
      PotentialRisk <|-- InabilityToFulfilLegalObligations
        click InabilityToFulfilLegalObligations href "../InabilityToFulfilLegalObligations/"
      PotentialRisk <|-- InabilityToProcessPayments
        click InabilityToProcessPayments href "../InabilityToProcessPayments/"
      PotentialRisk <|-- InabilityToProtectVitalInterests
        click InabilityToProtectVitalInterests href "../InabilityToProtectVitalInterests/"
      PotentialRisk <|-- InabilityToProvideHealthCare
        click InabilityToProvideHealthCare href "../InabilityToProvideHealthCare/"
      PotentialRisk <|-- IndirectDiscrimination
        click IndirectDiscrimination href "../IndirectDiscrimination/"
      PotentialRisk <|-- IndividualHealthSafety
        click IndividualHealthSafety href "../IndividualHealthSafety/"
      PotentialRisk <|-- IndividualRisk
        click IndividualRisk href "../IndividualRisk/"
      PotentialRisk <|-- InformativenessBias
        click InformativenessBias href "../InformativenessBias/"
      PotentialRisk <|-- Injury
        click Injury href "../Injury/"
      PotentialRisk <|-- InstructionsInaccessible
        click InstructionsInaccessible href "../InstructionsInaccessible/"
      PotentialRisk <|-- InstructionsIncorrect
        click InstructionsIncorrect href "../InstructionsIncorrect/"
      PotentialRisk <|-- InstructionsInsufficient
        click InstructionsInsufficient href "../InstructionsInsufficient/"
      PotentialRisk <|-- InstructionsUnsuitable
        click InstructionsUnsuitable href "../InstructionsUnsuitable/"
      PotentialRisk <|-- IntegrityBreach
        click IntegrityBreach href "../IntegrityBreach/"
      PotentialRisk <|-- IntentionalManipulation
        click IntentionalManipulation href "../IntentionalManipulation/"
      PotentialRisk <|-- IntentionalMisuse
        click IntentionalMisuse href "../IntentionalMisuse/"
      PotentialRisk <|-- InterceptCommunications
        click InterceptCommunications href "../InterceptCommunications/"
      PotentialRisk <|-- JudicialCosts
        click JudicialCosts href "../JudicialCosts/"
      PotentialRisk <|-- JudicialPenalty
        click JudicialPenalty href "../JudicialPenalty/"
      PotentialRisk <|-- LackOfSystemTransparency
        click LackOfSystemTransparency href "../LackOfSystemTransparency/"
      PotentialRisk <|-- LanguageDiscrimination
        click LanguageDiscrimination href "../LanguageDiscrimination/"
      PotentialRisk <|-- LegalComplianceRisk
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      PotentialRisk <|-- LegalRiskConcept
        click LegalRiskConcept href "../LegalRiskConcept/"
      PotentialRisk <|-- LegalSupportLimited
        click LegalSupportLimited href "../LegalSupportLimited/"
      PotentialRisk <|-- LegallyRelevantConsequence
        click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      PotentialRisk <|-- LoyaltyProgramExclusion
        click LoyaltyProgramExclusion href "../LoyaltyProgramExclusion/"
      PotentialRisk <|-- MaliciousActivity
        click MaliciousActivity href "../MaliciousActivity/"
      PotentialRisk <|-- MaliciousCodeAttack
        click MaliciousCodeAttack href "../MaliciousCodeAttack/"
      PotentialRisk <|-- MalwareAttack
        click MalwareAttack href "../MalwareAttack/"
      PotentialRisk <|-- MaterialDamage
        click MaterialDamage href "../MaterialDamage/"
      PotentialRisk <|-- MentalHealth
        click MentalHealth href "../MentalHealth/"
      PotentialRisk <|-- MentalSafety
        click MentalSafety href "../MentalSafety/"
      PotentialRisk <|-- Misandry
        click Misandry href "../Misandry/"
      PotentialRisk <|-- Misogyny
        click Misogyny href "../Misogyny/"
      PotentialRisk <|-- Misuse
        click Misuse href "../Misuse/"
      PotentialRisk <|-- NationalityDiscrimination
        click NationalityDiscrimination href "../NationalityDiscrimination/"
      PotentialRisk <|-- NegotiatingCapacityLoss
        click NegotiatingCapacityLoss href "../NegotiatingCapacityLoss/"
      PotentialRisk <|-- NonMaterialDamage
        click NonMaterialDamage href "../NonMaterialDamage/"
      PotentialRisk <|-- NonNormalityBias
        click NonNormalityBias href "../NonNormalityBias/"
      PotentialRisk <|-- NonResponseBias
        click NonResponseBias href "../NonResponseBias/"
      PotentialRisk <|-- OperationalSecurityRisk
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      PotentialRisk <|-- OpportunityLoss
        click OpportunityLoss href "../OpportunityLoss/"
      PotentialRisk <|-- OrganisationalManagementRisk
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      PotentialRisk <|-- OrganisationalRiskConcept
        click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      PotentialRisk <|-- OutGroupHomogeneityBias
        click OutGroupHomogeneityBias href "../OutGroupHomogeneityBias/"
      PotentialRisk <|-- Payment
        click Payment href "../Payment/"
      PotentialRisk <|-- PersonalSafetyEndangerment
        click PersonalSafetyEndangerment href "../PersonalSafetyEndangerment/"
      PotentialRisk <|-- PersonalisationDisabled
        click PersonalisationDisabled href "../PersonalisationDisabled/"
      PotentialRisk <|-- PersonalisationEnabled
        click PersonalisationEnabled href "../PersonalisationEnabled/"
      PotentialRisk <|-- PhishingScam
        click PhishingScam href "../PhishingScam/"
      PotentialRisk <|-- PhysicalAssault
        click PhysicalAssault href "../PhysicalAssault/"
      PotentialRisk <|-- PhysicalHarm
        click PhysicalHarm href "../PhysicalHarm/"
      PotentialRisk <|-- PhysicalHealth
        click PhysicalHealth href "../PhysicalHealth/"
      PotentialRisk <|-- PhysicalSafety
        click PhysicalSafety href "../PhysicalSafety/"
      PotentialRisk <|-- PolicyRisk
        click PolicyRisk href "../PolicyRisk/"
      PotentialRisk <|-- Privacy
        click Privacy href "../Privacy/"
      PotentialRisk <|-- PsychologicalHarm
        click PsychologicalHarm href "../PsychologicalHarm/"
      PotentialRisk <|-- PublicHealthSafety
        click PublicHealthSafety href "../PublicHealthSafety/"
      PotentialRisk <|-- PublicOrderBreach
        click PublicOrderBreach href "../PublicOrderBreach/"
      PotentialRisk <|-- PublicServicesExclusion
        click PublicServicesExclusion href "../PublicServicesExclusion/"
      PotentialRisk <|-- QualityDegraded
        click QualityDegraded href "../QualityDegraded/"
      PotentialRisk <|-- QualityInconsistent
        click QualityInconsistent href "../QualityInconsistent/"
      PotentialRisk <|-- QualityInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      PotentialRisk <|-- QualityRisk
        click QualityRisk href "../QualityRisk/"
      PotentialRisk <|-- QualityUnknown
        click QualityUnknown href "../QualityUnknown/"
      PotentialRisk <|-- QualityUnverified
        click QualityUnverified href "../QualityUnverified/"
      PotentialRisk <|-- RacialDiscrimination
        click RacialDiscrimination href "../RacialDiscrimination/"
      PotentialRisk <|-- Racism
        click Racism href "../Racism/"
      PotentialRisk <|-- Reidentification
        click Reidentification href "../Reidentification/"
      PotentialRisk <|-- ReligiousDiscrimination
        click ReligiousDiscrimination href "../ReligiousDiscrimination/"
      PotentialRisk <|-- Remuneration
        click Remuneration href "../Remuneration/"
      PotentialRisk <|-- ReputationalLoss
        click ReputationalLoss href "../ReputationalLoss/"
      PotentialRisk <|-- ReputationalRisk
        click ReputationalRisk href "../ReputationalRisk/"
      PotentialRisk <|-- RequirementsBias
        click RequirementsBias href "../RequirementsBias/"
      PotentialRisk <|-- ResilienceDegraded
        click ResilienceDegraded href "../ResilienceDegraded/"
      PotentialRisk <|-- ResilienceInconsistent
        click ResilienceInconsistent href "../ResilienceInconsistent/"
      PotentialRisk <|-- ResilienceInsufficient
        click ResilienceInsufficient href "../ResilienceInsufficient/"
      PotentialRisk <|-- ResilienceRisk
        click ResilienceRisk href "../ResilienceRisk/"
      PotentialRisk <|-- ResilienceUnknown
        click ResilienceUnknown href "../ResilienceUnknown/"
      PotentialRisk <|-- ResilienceUnverified
        click ResilienceUnverified href "../ResilienceUnverified/"
      PotentialRisk <|-- ReverseDiscrimination
        click ReverseDiscrimination href "../ReverseDiscrimination/"
      PotentialRisk <|-- Reward
        click Reward href "../Reward/"
      PotentialRisk <|-- RightsDenied
        click RightsDenied href "../RightsDenied/"
      PotentialRisk <|-- RightsEroded
        click RightsEroded href "../RightsEroded/"
      PotentialRisk <|-- RightsExercisePrevented
        click RightsExercisePrevented href "../RightsExercisePrevented/"
      PotentialRisk <|-- RightsImpact
        click RightsImpact href "../RightsImpact/"
      PotentialRisk <|-- RightsLimited
        click RightsLimited href "../RightsLimited/"
      PotentialRisk <|-- RightsObstructed
        click RightsObstructed href "../RightsObstructed/"
      PotentialRisk <|-- RightsUnfulfilled
        click RightsUnfulfilled href "../RightsUnfulfilled/"
      PotentialRisk <|-- RightsViolated
        click RightsViolated href "../RightsViolated/"
      PotentialRisk <|-- RobustnessDegraded
        click RobustnessDegraded href "../RobustnessDegraded/"
      PotentialRisk <|-- RobustnessInconsistent
        click RobustnessInconsistent href "../RobustnessInconsistent/"
      PotentialRisk <|-- RobustnessInsufficient
        click RobustnessInsufficient href "../RobustnessInsufficient/"
      PotentialRisk <|-- RobustnessRisk
        click RobustnessRisk href "../RobustnessRisk/"
      PotentialRisk <|-- RobustnessUnknown
        click RobustnessUnknown href "../RobustnessUnknown/"
      PotentialRisk <|-- RobustnessUnverified
        click RobustnessUnverified href "../RobustnessUnverified/"
      PotentialRisk <|-- RuleBasedSystemDesign
        click RuleBasedSystemDesign href "../RuleBasedSystemDesign/"
      PotentialRisk <|-- Sabotage
        click Sabotage href "../Sabotage/"
      PotentialRisk <|-- Safety
        click Safety href "../Safety/"
      PotentialRisk <|-- SamplingBias
        click SamplingBias href "../SamplingBias/"
      PotentialRisk <|-- Scam
        click Scam href "../Scam/"
      PotentialRisk <|-- SecurityAttack
        click SecurityAttack href "../SecurityAttack/"
      PotentialRisk <|-- SecurityBreach
        click SecurityBreach href "../SecurityBreach/"
      PotentialRisk <|-- SecurityQualityDegraded
        click SecurityQualityDegraded href "../SecurityQualityDegraded/"
      PotentialRisk <|-- SecurityQualityInconsistent
        click SecurityQualityInconsistent href "../SecurityQualityInconsistent/"
      PotentialRisk <|-- SecurityQualityInsufficient
        click SecurityQualityInsufficient href "../SecurityQualityInsufficient/"
      PotentialRisk <|-- SecurityQualityRisk
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      PotentialRisk <|-- SecurityQualityUnknown
        click SecurityQualityUnknown href "../SecurityQualityUnknown/"
      PotentialRisk <|-- SecurityQualityUnverified
        click SecurityQualityUnverified href "../SecurityQualityUnverified/"
      PotentialRisk <|-- SelectionBias
        click SelectionBias href "../SelectionBias/"
      PotentialRisk <|-- ServiceAlternativeOffered
        click ServiceAlternativeOffered href "../ServiceAlternativeOffered/"
      PotentialRisk <|-- ServiceCostIncreased
        click ServiceCostIncreased href "../ServiceCostIncreased/"
      PotentialRisk <|-- ServiceDenied
        click ServiceDenied href "../ServiceDenied/"
      PotentialRisk <|-- ServiceLimited
        click ServiceLimited href "../ServiceLimited/"
      PotentialRisk <|-- ServiceNotProvided
        click ServiceNotProvided href "../ServiceNotProvided/"
      PotentialRisk <|-- ServicePartiallyProvided
        click ServicePartiallyProvided href "../ServicePartiallyProvided/"
      PotentialRisk <|-- ServiceProvided
        click ServiceProvided href "../ServiceProvided/"
      PotentialRisk <|-- ServiceProvisionDelayed
        click ServiceProvisionDelayed href "../ServiceProvisionDelayed/"
      PotentialRisk <|-- ServiceQualityReduced
        click ServiceQualityReduced href "../ServiceQualityReduced/"
      PotentialRisk <|-- ServiceRelatedConsequence
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      PotentialRisk <|-- ServiceSecurityReduced
        click ServiceSecurityReduced href "../ServiceSecurityReduced/"
      PotentialRisk <|-- ServiceTermination
        click ServiceTermination href "../ServiceTermination/"
      PotentialRisk <|-- SexDiscrimination
        click SexDiscrimination href "../SexDiscrimination/"
      PotentialRisk <|-- Sexism
        click Sexism href "../Sexism/"
      PotentialRisk <|-- SexualHarassment
        click SexualHarassment href "../SexualHarassment/"
      PotentialRisk <|-- SexualOrientationDiscrimination
        click SexualOrientationDiscrimination href "../SexualOrientationDiscrimination/"
      PotentialRisk <|-- SexualViolence
        click SexualViolence href "../SexualViolence/"
      PotentialRisk <|-- SimpsonsParadoxBias
        click SimpsonsParadoxBias href "../SimpsonsParadoxBias/"
      PotentialRisk <|-- SocialDisadvantage
        click SocialDisadvantage href "../SocialDisadvantage/"
      PotentialRisk <|-- SocietalBias
        click SocietalBias href "../SocietalBias/"
      PotentialRisk <|-- SocietalHealthSafety
        click SocietalHealthSafety href "../SocietalHealthSafety/"
      PotentialRisk <|-- SocietalRiskConcept
        click SocietalRiskConcept href "../SocietalRiskConcept/"
      PotentialRisk <|-- Spoofing
        click Spoofing href "../Spoofing/"
      PotentialRisk <|-- StaffIncompetence
        click StaffIncompetence href "../StaffIncompetence/"
      PotentialRisk <|-- StatisticalBias
        click StatisticalBias href "../StatisticalBias/"
      PotentialRisk <|-- SystemFailure
        click SystemFailure href "../SystemFailure/"
      PotentialRisk <|-- SystemIntrusion
        click SystemIntrusion href "../SystemIntrusion/"
      PotentialRisk <|-- SystemMalfunction
        click SystemMalfunction href "../SystemMalfunction/"
      PotentialRisk <|-- TaskExecutionIncorrect
        click TaskExecutionIncorrect href "../TaskExecutionIncorrect/"
      PotentialRisk <|-- TaskExecutionRisk
        click TaskExecutionRisk href "../TaskExecutionRisk/"
      PotentialRisk <|-- TaskOmitted
        click TaskOmitted href "../TaskOmitted/"
      PotentialRisk <|-- TaskTimingIncorrect
        click TaskTimingIncorrect href "../TaskTimingIncorrect/"
      PotentialRisk <|-- TechnicalRiskConcept
        click TechnicalRiskConcept href "../TechnicalRiskConcept/"
      PotentialRisk <|-- TechnologyOverreliance
        click TechnologyOverreliance href "../TechnologyOverreliance/"
      PotentialRisk <|-- Terrorism
        click Terrorism href "../Terrorism/"
      PotentialRisk <|-- Transphobia
        click Transphobia href "../Transphobia/"
      PotentialRisk <|-- TrustLoss
        click TrustLoss href "../TrustLoss/"
      PotentialRisk <|-- UnauthorisedAccessToPremises
        click UnauthorisedAccessToPremises href "../UnauthorisedAccessToPremises/"
      PotentialRisk <|-- UnauthorisedActivity
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      PotentialRisk <|-- UnauthorisedCodeAccess
        click UnauthorisedCodeAccess href "../UnauthorisedCodeAccess/"
      PotentialRisk <|-- UnauthorisedCodeDisclosure
        click UnauthorisedCodeDisclosure href "../UnauthorisedCodeDisclosure/"
      PotentialRisk <|-- UnauthorisedCodeModification
        click UnauthorisedCodeModification href "../UnauthorisedCodeModification/"
      PotentialRisk <|-- UnauthorisedDataAccess
        click UnauthorisedDataAccess href "../UnauthorisedDataAccess/"
      PotentialRisk <|-- UnauthorisedDataDisclosure
        click UnauthorisedDataDisclosure href "../UnauthorisedDataDisclosure/"
      PotentialRisk <|-- UnauthorisedDataModification
        click UnauthorisedDataModification href "../UnauthorisedDataModification/"
      PotentialRisk <|-- UnauthorisedInformationDisclosure
        click UnauthorisedInformationDisclosure href "../UnauthorisedInformationDisclosure/"
      PotentialRisk <|-- UnauthorisedReidentification
        click UnauthorisedReidentification href "../UnauthorisedReidentification/"
      PotentialRisk <|-- UnauthorisedResourceUse
        click UnauthorisedResourceUse href "../UnauthorisedResourceUse/"
      PotentialRisk <|-- UnauthorisedSystemAccess
        click UnauthorisedSystemAccess href "../UnauthorisedSystemAccess/"
      PotentialRisk <|-- UnauthorisedSystemModification
        click UnauthorisedSystemModification href "../UnauthorisedSystemModification/"
      PotentialRisk <|-- UnfavourableTreatment
        click UnfavourableTreatment href "../UnfavourableTreatment/"
      PotentialRisk <|-- UnwantedCodeDeletion
        click UnwantedCodeDeletion href "../UnwantedCodeDeletion/"
      PotentialRisk <|-- UnwantedDataDeletion
        click UnwantedDataDeletion href "../UnwantedDataDeletion/"
      PotentialRisk <|-- UnwantedDisclosureData
        click UnwantedDisclosureData href "../UnwantedDisclosureData/"
      PotentialRisk <|-- UserRisks
        click UserRisks href "../UserRisks/"
      PotentialRisk <|-- ViolatingCodeOfConduct
        click ViolatingCodeOfConduct href "../ViolatingCodeOfConduct/"
      PotentialRisk <|-- ViolatingContractualObligation
        click ViolatingContractualObligation href "../ViolatingContractualObligation/"
      PotentialRisk <|-- ViolatingEthicsCode
        click ViolatingEthicsCode href "../ViolatingEthicsCode/"
      PotentialRisk <|-- ViolatingLegalObligation
        click ViolatingLegalObligation href "../ViolatingLegalObligation/"
      PotentialRisk <|-- ViolatingObligation
        click ViolatingObligation href "../ViolatingObligation/"
      PotentialRisk <|-- ViolatingPolicy
        click ViolatingPolicy href "../ViolatingPolicy/"
      PotentialRisk <|-- ViolatingProhibition
        click ViolatingProhibition href "../ViolatingProhibition/"
      PotentialRisk <|-- ViolatingStatutoryObligations
        click ViolatingStatutoryObligations href "../ViolatingStatutoryObligations/"
      PotentialRisk <|-- ViolenceAgainstChildren
        click ViolenceAgainstChildren href "../ViolenceAgainstChildren/"
      PotentialRisk <|-- VulnerabilityExploitation
        click VulnerabilityExploitation href "../VulnerabilityExploitation/"
      PotentialRisk <|-- Wellbeing
        click Wellbeing href "../Wellbeing/"
      PotentialRisk <|-- WorkplaceDiscrimination
        click WorkplaceDiscrimination href "../WorkplaceDiscrimination/"
      
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PotentialRisk](https://w3id.org/lmodel/dpv/risk/PotentialRisk) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Potential Risk


## Comments

* PotentialRisk is a suggestion that the concept can be a 'risk' within an
use-case - this suggestion is not exclusive and the concept may also be
instances of other potential concepts to indicate the multiple possible
roles a concept can take. This suggestion can be ignored if it is not
applicable to the use-case



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PotentialRisk |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PotentialRisk |
| native | risk:PotentialRisk |
| exact | dpv_risk:PotentialRisk, dpv_risk_owl:PotentialRisk |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PotentialRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PotentialRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates a concept can potentially be a ''risk'' concept within an

  use-case'
comments:
- 'PotentialRisk is a suggestion that the concept can be a ''risk'' within an

  use-case - this suggestion is not exclusive and the concept may also be

  instances of other potential concepts to indicate the multiple possible

  roles a concept can take. This suggestion can be ignored if it is not

  applicable to the use-case'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Potential Risk
exact_mappings:
- dpv_risk:PotentialRisk
- dpv_risk_owl:PotentialRisk
class_uri: risk:PotentialRisk

```
</details>

### Induced

<details>
```yaml
name: PotentialRisk
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PotentialRisk
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates a concept can potentially be a ''risk'' concept within an

  use-case'
comments:
- 'PotentialRisk is a suggestion that the concept can be a ''risk'' within an

  use-case - this suggestion is not exclusive and the concept may also be

  instances of other potential concepts to indicate the multiple possible

  roles a concept can take. This suggestion can be ignored if it is not

  applicable to the use-case'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Potential Risk
exact_mappings:
- dpv_risk:PotentialRisk
- dpv_risk_owl:PotentialRisk
class_uri: risk:PotentialRisk

```
</details></div>