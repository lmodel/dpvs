---
search:
  boost: 10.0
---

# Class: PotentialConsequence 


_Indicates a concept can potentially be a 'consequence concept within an_

_use-case_



<div data-search-exclude markdown="1">



URI: [risk:PotentialConsequence](https://w3id.org/lmodel/dpv/risk/PotentialConsequence)





```mermaid
 classDiagram
    class PotentialConsequence
    click PotentialConsequence href "../PotentialConsequence/"
      PotentialConsequence <|-- AccidentalMisuse
        click AccidentalMisuse href "../AccidentalMisuse/"
      PotentialConsequence <|-- AccuracyDegraded
        click AccuracyDegraded href "../AccuracyDegraded/"
      PotentialConsequence <|-- AccuracyInconsistent
        click AccuracyInconsistent href "../AccuracyInconsistent/"
      PotentialConsequence <|-- AccuracyInsufficient
        click AccuracyInsufficient href "../AccuracyInsufficient/"
      PotentialConsequence <|-- AccuracyRisk
        click AccuracyRisk href "../AccuracyRisk/"
      PotentialConsequence <|-- AccuracyUnknown
        click AccuracyUnknown href "../AccuracyUnknown/"
      PotentialConsequence <|-- AccuracyUnverified
        click AccuracyUnverified href "../AccuracyUnverified/"
      PotentialConsequence <|-- AgeDiscrimination
        click AgeDiscrimination href "../AgeDiscrimination/"
      PotentialConsequence <|-- AvailabilityBreach
        click AvailabilityBreach href "../AvailabilityBreach/"
      PotentialConsequence <|-- BehaviourDistortion
        click BehaviourDistortion href "../BehaviourDistortion/"
      PotentialConsequence <|-- BelievesDiscrimination
        click BelievesDiscrimination href "../BelievesDiscrimination/"
      PotentialConsequence <|-- Benefit
        click Benefit href "../Benefit/"
      PotentialConsequence <|-- Bias
        click Bias href "../Bias/"
      PotentialConsequence <|-- Blackmail
        click Blackmail href "../Blackmail/"
      PotentialConsequence <|-- CasteDiscrimination
        click CasteDiscrimination href "../CasteDiscrimination/"
      PotentialConsequence <|-- Coercion
        click Coercion href "../Coercion/"
      PotentialConsequence <|-- CognitiveBias
        click CognitiveBias href "../CognitiveBias/"
      PotentialConsequence <|-- Compensation
        click Compensation href "../Compensation/"
      PotentialConsequence <|-- ComponentFailure
        click ComponentFailure href "../ComponentFailure/"
      PotentialConsequence <|-- ComponentMalfunction
        click ComponentMalfunction href "../ComponentMalfunction/"
      PotentialConsequence <|-- CompromiseAccount
        click CompromiseAccount href "../CompromiseAccount/"
      PotentialConsequence <|-- CompromiseAccountCredentials
        click CompromiseAccountCredentials href "../CompromiseAccountCredentials/"
      PotentialConsequence <|-- ConfidentialityBreach
        click ConfidentialityBreach href "../ConfidentialityBreach/"
      PotentialConsequence <|-- ConfirmationBias
        click ConfirmationBias href "../ConfirmationBias/"
      PotentialConsequence <|-- ConfoundingVariablesBias
        click ConfoundingVariablesBias href "../ConfoundingVariablesBias/"
      PotentialConsequence <|-- CopyrightViolation
        click CopyrightViolation href "../CopyrightViolation/"
      PotentialConsequence <|-- CoverageBias
        click CoverageBias href "../CoverageBias/"
      PotentialConsequence <|-- CredibilityLoss
        click CredibilityLoss href "../CredibilityLoss/"
      PotentialConsequence <|-- CustomerConfidenceLoss
        click CustomerConfidenceLoss href "../CustomerConfidenceLoss/"
      PotentialConsequence <|-- CustomerSupportLimited
        click CustomerSupportLimited href "../CustomerSupportLimited/"
      PotentialConsequence <|-- Damage
        click Damage href "../Damage/"
      PotentialConsequence <|-- DataAggregationBias
        click DataAggregationBias href "../DataAggregationBias/"
      PotentialConsequence <|-- DataBias
        click DataBias href "../DataBias/"
      PotentialConsequence <|-- DataBreach
        click DataBreach href "../DataBreach/"
      PotentialConsequence <|-- DataCollectionError
        click DataCollectionError href "../DataCollectionError/"
      PotentialConsequence <|-- DataCorruption
        click DataCorruption href "../DataCorruption/"
      PotentialConsequence <|-- DataErasureError
        click DataErasureError href "../DataErasureError/"
      PotentialConsequence <|-- DataInaccurate
        click DataInaccurate href "../DataInaccurate/"
      PotentialConsequence <|-- DataIncomplete
        click DataIncomplete href "../DataIncomplete/"
      PotentialConsequence <|-- DataInconsistent
        click DataInconsistent href "../DataInconsistent/"
      PotentialConsequence <|-- DataLoss
        click DataLoss href "../DataLoss/"
      PotentialConsequence <|-- DataMisclassified
        click DataMisclassified href "../DataMisclassified/"
      PotentialConsequence <|-- DataMisinterpretation
        click DataMisinterpretation href "../DataMisinterpretation/"
      PotentialConsequence <|-- DataNoise
        click DataNoise href "../DataNoise/"
      PotentialConsequence <|-- DataOutdated
        click DataOutdated href "../DataOutdated/"
      PotentialConsequence <|-- DataPreparationError
        click DataPreparationError href "../DataPreparationError/"
      PotentialConsequence <|-- DataProcessingBias
        click DataProcessingBias href "../DataProcessingBias/"
      PotentialConsequence <|-- DataProcessingError
        click DataProcessingError href "../DataProcessingError/"
      PotentialConsequence <|-- DataRisk
        click DataRisk href "../DataRisk/"
      PotentialConsequence <|-- DataSelectionError
        click DataSelectionError href "../DataSelectionError/"
      PotentialConsequence <|-- DataSparse
        click DataSparse href "../DataSparse/"
      PotentialConsequence <|-- DataStorageError
        click DataStorageError href "../DataStorageError/"
      PotentialConsequence <|-- DataTransferError
        click DataTransferError href "../DataTransferError/"
      PotentialConsequence <|-- DataUnavailable
        click DataUnavailable href "../DataUnavailable/"
      PotentialConsequence <|-- DataUnrepresentative
        click DataUnrepresentative href "../DataUnrepresentative/"
      PotentialConsequence <|-- DataUnstructured
        click DataUnstructured href "../DataUnstructured/"
      PotentialConsequence <|-- DataUnverified
        click DataUnverified href "../DataUnverified/"
      PotentialConsequence <|-- Deception
        click Deception href "../Deception/"
      PotentialConsequence <|-- DelayedApplicationProcessing
        click DelayedApplicationProcessing href "../DelayedApplicationProcessing/"
      PotentialConsequence <|-- Detriment
        click Detriment href "../Detriment/"
      PotentialConsequence <|-- DirectDiscrimination
        click DirectDiscrimination href "../DirectDiscrimination/"
      PotentialConsequence <|-- DisabilityDiscrimination
        click DisabilityDiscrimination href "../DisabilityDiscrimination/"
      PotentialConsequence <|-- Discrimination
        click Discrimination href "../Discrimination/"
      PotentialConsequence <|-- DisproportionateEnergyConsumption
        click DisproportionateEnergyConsumption href "../DisproportionateEnergyConsumption/"
      PotentialConsequence <|-- DocumentationIssues
        click DocumentationIssues href "../DocumentationIssues/"
      PotentialConsequence <|-- Earthquake
        click Earthquake href "../Earthquake/"
      PotentialConsequence <|-- EnvironmentalRisk
        click EnvironmentalRisk href "../EnvironmentalRisk/"
      PotentialConsequence <|-- EquipmentFailure
        click EquipmentFailure href "../EquipmentFailure/"
      PotentialConsequence <|-- EquipmentMalfunction
        click EquipmentMalfunction href "../EquipmentMalfunction/"
      PotentialConsequence <|-- ErroneousUse
        click ErroneousUse href "../ErroneousUse/"
      PotentialConsequence <|-- EthnicDiscrimination
        click EthnicDiscrimination href "../EthnicDiscrimination/"
      PotentialConsequence <|-- ExcellenceDiscrimination
        click ExcellenceDiscrimination href "../ExcellenceDiscrimination/"
      PotentialConsequence <|-- Exploitation
        click Exploitation href "../Exploitation/"
      PotentialConsequence <|-- ExposureToHarmfulSpeech
        click ExposureToHarmfulSpeech href "../ExposureToHarmfulSpeech/"
      PotentialConsequence <|-- ExternalSecurityThreat
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      PotentialConsequence <|-- Extortion
        click Extortion href "../Extortion/"
      PotentialConsequence <|-- FinancialImpact
        click FinancialImpact href "../FinancialImpact/"
      PotentialConsequence <|-- FinancialLoss
        click FinancialLoss href "../FinancialLoss/"
      PotentialConsequence <|-- Floods
        click Floods href "../Floods/"
      PotentialConsequence <|-- Fraud
        click Fraud href "../Fraud/"
      PotentialConsequence <|-- GenderDiscrimination
        click GenderDiscrimination href "../GenderDiscrimination/"
      PotentialConsequence <|-- GeographicDiscrimination
        click GeographicDiscrimination href "../GeographicDiscrimination/"
      PotentialConsequence <|-- GoodwillLoss
        click GoodwillLoss href "../GoodwillLoss/"
      PotentialConsequence <|-- GroupAttributionBias
        click GroupAttributionBias href "../GroupAttributionBias/"
      PotentialConsequence <|-- GroupHealthSafety
        click GroupHealthSafety href "../GroupHealthSafety/"
      PotentialConsequence <|-- GroupRisk
        click GroupRisk href "../GroupRisk/"
      PotentialConsequence <|-- Harassment
        click Harassment href "../Harassment/"
      PotentialConsequence <|-- Harm
        click Harm href "../Harm/"
      PotentialConsequence <|-- Health
        click Health href "../Health/"
      PotentialConsequence <|-- HealthSafety
        click HealthSafety href "../HealthSafety/"
      PotentialConsequence <|-- Homophobia
        click Homophobia href "../Homophobia/"
      PotentialConsequence <|-- HumanErrors
        click HumanErrors href "../HumanErrors/"
      PotentialConsequence <|-- HumanOversightIneffective
        click HumanOversightIneffective href "../HumanOversightIneffective/"
      PotentialConsequence <|-- HumanOversightInsufficient
        click HumanOversightInsufficient href "../HumanOversightInsufficient/"
      PotentialConsequence <|-- IdentityFraud
        click IdentityFraud href "../IdentityFraud/"
      PotentialConsequence <|-- IdentityTheft
        click IdentityTheft href "../IdentityTheft/"
      PotentialConsequence <|-- IdentityVerificationFailure
        click IdentityVerificationFailure href "../IdentityVerificationFailure/"
      PotentialConsequence <|-- IllegalDataProcessing
        click IllegalDataProcessing href "../IllegalDataProcessing/"
      PotentialConsequence <|-- ImpairedDecisionMaking
        click ImpairedDecisionMaking href "../ImpairedDecisionMaking/"
      PotentialConsequence <|-- ImplicitBias
        click ImplicitBias href "../ImplicitBias/"
      PotentialConsequence <|-- InGroupBias
        click InGroupBias href "../InGroupBias/"
      PotentialConsequence <|-- InabilityToEnterIntoContract
        click InabilityToEnterIntoContract href "../InabilityToEnterIntoContract/"
      PotentialConsequence <|-- InabilityToEstablishLegalClaims
        click InabilityToEstablishLegalClaims href "../InabilityToEstablishLegalClaims/"
      PotentialConsequence <|-- InabilityToFulfilLegalObligations
        click InabilityToFulfilLegalObligations href "../InabilityToFulfilLegalObligations/"
      PotentialConsequence <|-- InabilityToProcessPayments
        click InabilityToProcessPayments href "../InabilityToProcessPayments/"
      PotentialConsequence <|-- InabilityToProtectVitalInterests
        click InabilityToProtectVitalInterests href "../InabilityToProtectVitalInterests/"
      PotentialConsequence <|-- InabilityToProvideHealthCare
        click InabilityToProvideHealthCare href "../InabilityToProvideHealthCare/"
      PotentialConsequence <|-- IndirectDiscrimination
        click IndirectDiscrimination href "../IndirectDiscrimination/"
      PotentialConsequence <|-- IndividualHealthSafety
        click IndividualHealthSafety href "../IndividualHealthSafety/"
      PotentialConsequence <|-- IndividualRisk
        click IndividualRisk href "../IndividualRisk/"
      PotentialConsequence <|-- InformativenessBias
        click InformativenessBias href "../InformativenessBias/"
      PotentialConsequence <|-- Injury
        click Injury href "../Injury/"
      PotentialConsequence <|-- InstructionsInaccessible
        click InstructionsInaccessible href "../InstructionsInaccessible/"
      PotentialConsequence <|-- InstructionsIncorrect
        click InstructionsIncorrect href "../InstructionsIncorrect/"
      PotentialConsequence <|-- InstructionsInsufficient
        click InstructionsInsufficient href "../InstructionsInsufficient/"
      PotentialConsequence <|-- InstructionsUnsuitable
        click InstructionsUnsuitable href "../InstructionsUnsuitable/"
      PotentialConsequence <|-- IntegrityBreach
        click IntegrityBreach href "../IntegrityBreach/"
      PotentialConsequence <|-- IntentionalManipulation
        click IntentionalManipulation href "../IntentionalManipulation/"
      PotentialConsequence <|-- IntentionalMisuse
        click IntentionalMisuse href "../IntentionalMisuse/"
      PotentialConsequence <|-- InterceptCommunications
        click InterceptCommunications href "../InterceptCommunications/"
      PotentialConsequence <|-- JudicialCosts
        click JudicialCosts href "../JudicialCosts/"
      PotentialConsequence <|-- JudicialPenalty
        click JudicialPenalty href "../JudicialPenalty/"
      PotentialConsequence <|-- LackOfSystemTransparency
        click LackOfSystemTransparency href "../LackOfSystemTransparency/"
      PotentialConsequence <|-- LanguageDiscrimination
        click LanguageDiscrimination href "../LanguageDiscrimination/"
      PotentialConsequence <|-- LegalComplianceRisk
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      PotentialConsequence <|-- LegalRiskConcept
        click LegalRiskConcept href "../LegalRiskConcept/"
      PotentialConsequence <|-- LegalSupportLimited
        click LegalSupportLimited href "../LegalSupportLimited/"
      PotentialConsequence <|-- LegallyRelevantConsequence
        click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      PotentialConsequence <|-- LoyaltyProgramExclusion
        click LoyaltyProgramExclusion href "../LoyaltyProgramExclusion/"
      PotentialConsequence <|-- MaliciousActivity
        click MaliciousActivity href "../MaliciousActivity/"
      PotentialConsequence <|-- MaterialDamage
        click MaterialDamage href "../MaterialDamage/"
      PotentialConsequence <|-- MentalHealth
        click MentalHealth href "../MentalHealth/"
      PotentialConsequence <|-- MentalSafety
        click MentalSafety href "../MentalSafety/"
      PotentialConsequence <|-- Misandry
        click Misandry href "../Misandry/"
      PotentialConsequence <|-- Misogyny
        click Misogyny href "../Misogyny/"
      PotentialConsequence <|-- Misuse
        click Misuse href "../Misuse/"
      PotentialConsequence <|-- NationalityDiscrimination
        click NationalityDiscrimination href "../NationalityDiscrimination/"
      PotentialConsequence <|-- NegotiatingCapacityLoss
        click NegotiatingCapacityLoss href "../NegotiatingCapacityLoss/"
      PotentialConsequence <|-- NonMaterialDamage
        click NonMaterialDamage href "../NonMaterialDamage/"
      PotentialConsequence <|-- NonNormalityBias
        click NonNormalityBias href "../NonNormalityBias/"
      PotentialConsequence <|-- NonResponseBias
        click NonResponseBias href "../NonResponseBias/"
      PotentialConsequence <|-- OperationalSecurityRisk
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      PotentialConsequence <|-- OpportunityLoss
        click OpportunityLoss href "../OpportunityLoss/"
      PotentialConsequence <|-- OrganisationalManagementRisk
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      PotentialConsequence <|-- OrganisationalRiskConcept
        click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      PotentialConsequence <|-- OutGroupHomogeneityBias
        click OutGroupHomogeneityBias href "../OutGroupHomogeneityBias/"
      PotentialConsequence <|-- Payment
        click Payment href "../Payment/"
      PotentialConsequence <|-- PersonalSafetyEndangerment
        click PersonalSafetyEndangerment href "../PersonalSafetyEndangerment/"
      PotentialConsequence <|-- PersonalisationDisabled
        click PersonalisationDisabled href "../PersonalisationDisabled/"
      PotentialConsequence <|-- PersonalisationEnabled
        click PersonalisationEnabled href "../PersonalisationEnabled/"
      PotentialConsequence <|-- PhishingScam
        click PhishingScam href "../PhishingScam/"
      PotentialConsequence <|-- PhysicalAssault
        click PhysicalAssault href "../PhysicalAssault/"
      PotentialConsequence <|-- PhysicalHarm
        click PhysicalHarm href "../PhysicalHarm/"
      PotentialConsequence <|-- PhysicalHealth
        click PhysicalHealth href "../PhysicalHealth/"
      PotentialConsequence <|-- PhysicalSafety
        click PhysicalSafety href "../PhysicalSafety/"
      PotentialConsequence <|-- PolicyRisk
        click PolicyRisk href "../PolicyRisk/"
      PotentialConsequence <|-- Privacy
        click Privacy href "../Privacy/"
      PotentialConsequence <|-- PsychologicalHarm
        click PsychologicalHarm href "../PsychologicalHarm/"
      PotentialConsequence <|-- PublicHealthSafety
        click PublicHealthSafety href "../PublicHealthSafety/"
      PotentialConsequence <|-- PublicOrderBreach
        click PublicOrderBreach href "../PublicOrderBreach/"
      PotentialConsequence <|-- PublicServicesExclusion
        click PublicServicesExclusion href "../PublicServicesExclusion/"
      PotentialConsequence <|-- QualityDegraded
        click QualityDegraded href "../QualityDegraded/"
      PotentialConsequence <|-- QualityInconsistent
        click QualityInconsistent href "../QualityInconsistent/"
      PotentialConsequence <|-- QualityInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      PotentialConsequence <|-- QualityRisk
        click QualityRisk href "../QualityRisk/"
      PotentialConsequence <|-- QualityUnknown
        click QualityUnknown href "../QualityUnknown/"
      PotentialConsequence <|-- QualityUnverified
        click QualityUnverified href "../QualityUnverified/"
      PotentialConsequence <|-- RacialDiscrimination
        click RacialDiscrimination href "../RacialDiscrimination/"
      PotentialConsequence <|-- Racism
        click Racism href "../Racism/"
      PotentialConsequence <|-- Reidentification
        click Reidentification href "../Reidentification/"
      PotentialConsequence <|-- ReligiousDiscrimination
        click ReligiousDiscrimination href "../ReligiousDiscrimination/"
      PotentialConsequence <|-- Remuneration
        click Remuneration href "../Remuneration/"
      PotentialConsequence <|-- ReputationalLoss
        click ReputationalLoss href "../ReputationalLoss/"
      PotentialConsequence <|-- ReputationalRisk
        click ReputationalRisk href "../ReputationalRisk/"
      PotentialConsequence <|-- RequirementsBias
        click RequirementsBias href "../RequirementsBias/"
      PotentialConsequence <|-- ResilienceDegraded
        click ResilienceDegraded href "../ResilienceDegraded/"
      PotentialConsequence <|-- ResilienceInconsistent
        click ResilienceInconsistent href "../ResilienceInconsistent/"
      PotentialConsequence <|-- ResilienceInsufficient
        click ResilienceInsufficient href "../ResilienceInsufficient/"
      PotentialConsequence <|-- ResilienceRisk
        click ResilienceRisk href "../ResilienceRisk/"
      PotentialConsequence <|-- ResilienceUnknown
        click ResilienceUnknown href "../ResilienceUnknown/"
      PotentialConsequence <|-- ResilienceUnverified
        click ResilienceUnverified href "../ResilienceUnverified/"
      PotentialConsequence <|-- ReverseDiscrimination
        click ReverseDiscrimination href "../ReverseDiscrimination/"
      PotentialConsequence <|-- Reward
        click Reward href "../Reward/"
      PotentialConsequence <|-- RightsDenied
        click RightsDenied href "../RightsDenied/"
      PotentialConsequence <|-- RightsEroded
        click RightsEroded href "../RightsEroded/"
      PotentialConsequence <|-- RightsExercisePrevented
        click RightsExercisePrevented href "../RightsExercisePrevented/"
      PotentialConsequence <|-- RightsImpact
        click RightsImpact href "../RightsImpact/"
      PotentialConsequence <|-- RightsLimited
        click RightsLimited href "../RightsLimited/"
      PotentialConsequence <|-- RightsObstructed
        click RightsObstructed href "../RightsObstructed/"
      PotentialConsequence <|-- RightsUnfulfilled
        click RightsUnfulfilled href "../RightsUnfulfilled/"
      PotentialConsequence <|-- RightsViolated
        click RightsViolated href "../RightsViolated/"
      PotentialConsequence <|-- RobustnessDegraded
        click RobustnessDegraded href "../RobustnessDegraded/"
      PotentialConsequence <|-- RobustnessInconsistent
        click RobustnessInconsistent href "../RobustnessInconsistent/"
      PotentialConsequence <|-- RobustnessInsufficient
        click RobustnessInsufficient href "../RobustnessInsufficient/"
      PotentialConsequence <|-- RobustnessRisk
        click RobustnessRisk href "../RobustnessRisk/"
      PotentialConsequence <|-- RobustnessUnknown
        click RobustnessUnknown href "../RobustnessUnknown/"
      PotentialConsequence <|-- RobustnessUnverified
        click RobustnessUnverified href "../RobustnessUnverified/"
      PotentialConsequence <|-- RuleBasedSystemDesign
        click RuleBasedSystemDesign href "../RuleBasedSystemDesign/"
      PotentialConsequence <|-- Sabotage
        click Sabotage href "../Sabotage/"
      PotentialConsequence <|-- Safety
        click Safety href "../Safety/"
      PotentialConsequence <|-- SamplingBias
        click SamplingBias href "../SamplingBias/"
      PotentialConsequence <|-- Scam
        click Scam href "../Scam/"
      PotentialConsequence <|-- SecurityBreach
        click SecurityBreach href "../SecurityBreach/"
      PotentialConsequence <|-- SecurityQualityDegraded
        click SecurityQualityDegraded href "../SecurityQualityDegraded/"
      PotentialConsequence <|-- SecurityQualityInconsistent
        click SecurityQualityInconsistent href "../SecurityQualityInconsistent/"
      PotentialConsequence <|-- SecurityQualityInsufficient
        click SecurityQualityInsufficient href "../SecurityQualityInsufficient/"
      PotentialConsequence <|-- SecurityQualityRisk
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      PotentialConsequence <|-- SecurityQualityUnknown
        click SecurityQualityUnknown href "../SecurityQualityUnknown/"
      PotentialConsequence <|-- SecurityQualityUnverified
        click SecurityQualityUnverified href "../SecurityQualityUnverified/"
      PotentialConsequence <|-- SelectionBias
        click SelectionBias href "../SelectionBias/"
      PotentialConsequence <|-- ServiceAlternativeOffered
        click ServiceAlternativeOffered href "../ServiceAlternativeOffered/"
      PotentialConsequence <|-- ServiceCostIncreased
        click ServiceCostIncreased href "../ServiceCostIncreased/"
      PotentialConsequence <|-- ServiceDenied
        click ServiceDenied href "../ServiceDenied/"
      PotentialConsequence <|-- ServiceLimited
        click ServiceLimited href "../ServiceLimited/"
      PotentialConsequence <|-- ServiceNotProvided
        click ServiceNotProvided href "../ServiceNotProvided/"
      PotentialConsequence <|-- ServicePartiallyProvided
        click ServicePartiallyProvided href "../ServicePartiallyProvided/"
      PotentialConsequence <|-- ServiceProvided
        click ServiceProvided href "../ServiceProvided/"
      PotentialConsequence <|-- ServiceProvisionDelayed
        click ServiceProvisionDelayed href "../ServiceProvisionDelayed/"
      PotentialConsequence <|-- ServiceQualityReduced
        click ServiceQualityReduced href "../ServiceQualityReduced/"
      PotentialConsequence <|-- ServiceRelatedConsequence
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      PotentialConsequence <|-- ServiceSecurityReduced
        click ServiceSecurityReduced href "../ServiceSecurityReduced/"
      PotentialConsequence <|-- ServiceTermination
        click ServiceTermination href "../ServiceTermination/"
      PotentialConsequence <|-- SexDiscrimination
        click SexDiscrimination href "../SexDiscrimination/"
      PotentialConsequence <|-- Sexism
        click Sexism href "../Sexism/"
      PotentialConsequence <|-- SexualHarassment
        click SexualHarassment href "../SexualHarassment/"
      PotentialConsequence <|-- SexualOrientationDiscrimination
        click SexualOrientationDiscrimination href "../SexualOrientationDiscrimination/"
      PotentialConsequence <|-- SexualViolence
        click SexualViolence href "../SexualViolence/"
      PotentialConsequence <|-- SimpsonsParadoxBias
        click SimpsonsParadoxBias href "../SimpsonsParadoxBias/"
      PotentialConsequence <|-- SocialDisadvantage
        click SocialDisadvantage href "../SocialDisadvantage/"
      PotentialConsequence <|-- SocietalBias
        click SocietalBias href "../SocietalBias/"
      PotentialConsequence <|-- SocietalHealthSafety
        click SocietalHealthSafety href "../SocietalHealthSafety/"
      PotentialConsequence <|-- SocietalRiskConcept
        click SocietalRiskConcept href "../SocietalRiskConcept/"
      PotentialConsequence <|-- Spoofing
        click Spoofing href "../Spoofing/"
      PotentialConsequence <|-- StaffIncompetence
        click StaffIncompetence href "../StaffIncompetence/"
      PotentialConsequence <|-- StatisticalBias
        click StatisticalBias href "../StatisticalBias/"
      PotentialConsequence <|-- SystemFailure
        click SystemFailure href "../SystemFailure/"
      PotentialConsequence <|-- SystemMalfunction
        click SystemMalfunction href "../SystemMalfunction/"
      PotentialConsequence <|-- TaskExecutionIncorrect
        click TaskExecutionIncorrect href "../TaskExecutionIncorrect/"
      PotentialConsequence <|-- TaskExecutionRisk
        click TaskExecutionRisk href "../TaskExecutionRisk/"
      PotentialConsequence <|-- TaskOmitted
        click TaskOmitted href "../TaskOmitted/"
      PotentialConsequence <|-- TaskTimingIncorrect
        click TaskTimingIncorrect href "../TaskTimingIncorrect/"
      PotentialConsequence <|-- TechnicalRiskConcept
        click TechnicalRiskConcept href "../TechnicalRiskConcept/"
      PotentialConsequence <|-- TechnologyOverreliance
        click TechnologyOverreliance href "../TechnologyOverreliance/"
      PotentialConsequence <|-- Terrorism
        click Terrorism href "../Terrorism/"
      PotentialConsequence <|-- Transphobia
        click Transphobia href "../Transphobia/"
      PotentialConsequence <|-- TrustLoss
        click TrustLoss href "../TrustLoss/"
      PotentialConsequence <|-- UnauthorisedAccessToPremises
        click UnauthorisedAccessToPremises href "../UnauthorisedAccessToPremises/"
      PotentialConsequence <|-- UnauthorisedActivity
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      PotentialConsequence <|-- UnauthorisedCodeAccess
        click UnauthorisedCodeAccess href "../UnauthorisedCodeAccess/"
      PotentialConsequence <|-- UnauthorisedCodeDisclosure
        click UnauthorisedCodeDisclosure href "../UnauthorisedCodeDisclosure/"
      PotentialConsequence <|-- UnauthorisedCodeModification
        click UnauthorisedCodeModification href "../UnauthorisedCodeModification/"
      PotentialConsequence <|-- UnauthorisedDataAccess
        click UnauthorisedDataAccess href "../UnauthorisedDataAccess/"
      PotentialConsequence <|-- UnauthorisedDataDisclosure
        click UnauthorisedDataDisclosure href "../UnauthorisedDataDisclosure/"
      PotentialConsequence <|-- UnauthorisedDataModification
        click UnauthorisedDataModification href "../UnauthorisedDataModification/"
      PotentialConsequence <|-- UnauthorisedInformationDisclosure
        click UnauthorisedInformationDisclosure href "../UnauthorisedInformationDisclosure/"
      PotentialConsequence <|-- UnauthorisedReidentification
        click UnauthorisedReidentification href "../UnauthorisedReidentification/"
      PotentialConsequence <|-- UnauthorisedResourceUse
        click UnauthorisedResourceUse href "../UnauthorisedResourceUse/"
      PotentialConsequence <|-- UnauthorisedSystemAccess
        click UnauthorisedSystemAccess href "../UnauthorisedSystemAccess/"
      PotentialConsequence <|-- UnauthorisedSystemModification
        click UnauthorisedSystemModification href "../UnauthorisedSystemModification/"
      PotentialConsequence <|-- UnfavourableTreatment
        click UnfavourableTreatment href "../UnfavourableTreatment/"
      PotentialConsequence <|-- UnwantedCodeDeletion
        click UnwantedCodeDeletion href "../UnwantedCodeDeletion/"
      PotentialConsequence <|-- UnwantedDataDeletion
        click UnwantedDataDeletion href "../UnwantedDataDeletion/"
      PotentialConsequence <|-- UnwantedDisclosureData
        click UnwantedDisclosureData href "../UnwantedDisclosureData/"
      PotentialConsequence <|-- UserRisks
        click UserRisks href "../UserRisks/"
      PotentialConsequence <|-- ViolatingCodeOfConduct
        click ViolatingCodeOfConduct href "../ViolatingCodeOfConduct/"
      PotentialConsequence <|-- ViolatingContractualObligation
        click ViolatingContractualObligation href "../ViolatingContractualObligation/"
      PotentialConsequence <|-- ViolatingEthicsCode
        click ViolatingEthicsCode href "../ViolatingEthicsCode/"
      PotentialConsequence <|-- ViolatingLegalObligation
        click ViolatingLegalObligation href "../ViolatingLegalObligation/"
      PotentialConsequence <|-- ViolatingObligation
        click ViolatingObligation href "../ViolatingObligation/"
      PotentialConsequence <|-- ViolatingPolicy
        click ViolatingPolicy href "../ViolatingPolicy/"
      PotentialConsequence <|-- ViolatingProhibition
        click ViolatingProhibition href "../ViolatingProhibition/"
      PotentialConsequence <|-- ViolatingStatutoryObligations
        click ViolatingStatutoryObligations href "../ViolatingStatutoryObligations/"
      PotentialConsequence <|-- ViolenceAgainstChildren
        click ViolenceAgainstChildren href "../ViolenceAgainstChildren/"
      PotentialConsequence <|-- VulnerabilityExploitation
        click VulnerabilityExploitation href "../VulnerabilityExploitation/"
      PotentialConsequence <|-- Wellbeing
        click Wellbeing href "../Wellbeing/"
      PotentialConsequence <|-- WorkplaceDiscrimination
        click WorkplaceDiscrimination href "../WorkplaceDiscrimination/"
      
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PotentialConsequence](https://w3id.org/lmodel/dpv/risk/PotentialConsequence) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Potential Consequence


## Comments

* PotentialConsequence is a suggestion that the concept can be a 'risk'
within an use-case - this suggestion is not exclusive and the concept
may also be instances of other potential concepts to indicate the
multiple possible roles a concept can take. This suggestion can be
ignored if it is not applicable to the use-case



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PotentialConsequence |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PotentialConsequence |
| native | risk:PotentialConsequence |
| exact | dpv_risk:PotentialConsequence, dpv_risk_owl:PotentialConsequence |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PotentialConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PotentialConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates a concept can potentially be a ''consequence concept within
  an

  use-case'
comments:
- 'PotentialConsequence is a suggestion that the concept can be a ''risk''

  within an use-case - this suggestion is not exclusive and the concept

  may also be instances of other potential concepts to indicate the

  multiple possible roles a concept can take. This suggestion can be

  ignored if it is not applicable to the use-case'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Potential Consequence
exact_mappings:
- dpv_risk:PotentialConsequence
- dpv_risk_owl:PotentialConsequence
class_uri: risk:PotentialConsequence

```
</details>

### Induced

<details>
```yaml
name: PotentialConsequence
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PotentialConsequence
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates a concept can potentially be a ''consequence concept within
  an

  use-case'
comments:
- 'PotentialConsequence is a suggestion that the concept can be a ''risk''

  within an use-case - this suggestion is not exclusive and the concept

  may also be instances of other potential concepts to indicate the

  multiple possible roles a concept can take. This suggestion can be

  ignored if it is not applicable to the use-case'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Potential Consequence
exact_mappings:
- dpv_risk:PotentialConsequence
- dpv_risk_owl:PotentialConsequence
class_uri: risk:PotentialConsequence

```
</details></div>