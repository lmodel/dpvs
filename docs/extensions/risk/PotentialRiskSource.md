---
search:
  boost: 10.0
---

# Class: PotentialRiskSource 


_Indicates a concept can potentially be a 'risk source' concept within an_

_use-case_



<div data-search-exclude markdown="1">



URI: [risk:PotentialRiskSource](https://w3id.org/lmodel/dpv/risk/PotentialRiskSource)





```mermaid
 classDiagram
    class PotentialRiskSource
    click PotentialRiskSource href "../PotentialRiskSource/"
      PotentialRiskSource <|-- AccidentalMisuse
        click AccidentalMisuse href "../AccidentalMisuse/"
      PotentialRiskSource <|-- AccuracyDegraded
        click AccuracyDegraded href "../AccuracyDegraded/"
      PotentialRiskSource <|-- AccuracyInconsistent
        click AccuracyInconsistent href "../AccuracyInconsistent/"
      PotentialRiskSource <|-- AccuracyInsufficient
        click AccuracyInsufficient href "../AccuracyInsufficient/"
      PotentialRiskSource <|-- AccuracyRisk
        click AccuracyRisk href "../AccuracyRisk/"
      PotentialRiskSource <|-- AccuracyUnknown
        click AccuracyUnknown href "../AccuracyUnknown/"
      PotentialRiskSource <|-- AccuracyUnverified
        click AccuracyUnverified href "../AccuracyUnverified/"
      PotentialRiskSource <|-- AuthorisationFailure
        click AuthorisationFailure href "../AuthorisationFailure/"
      PotentialRiskSource <|-- AvailabilityBreach
        click AvailabilityBreach href "../AvailabilityBreach/"
      PotentialRiskSource <|-- Bias
        click Bias href "../Bias/"
      PotentialRiskSource <|-- Blackmail
        click Blackmail href "../Blackmail/"
      PotentialRiskSource <|-- BruteForceAuthorisations
        click BruteForceAuthorisations href "../BruteForceAuthorisations/"
      PotentialRiskSource <|-- Coercion
        click Coercion href "../Coercion/"
      PotentialRiskSource <|-- CognitiveBias
        click CognitiveBias href "../CognitiveBias/"
      PotentialRiskSource <|-- ComponentFailure
        click ComponentFailure href "../ComponentFailure/"
      PotentialRiskSource <|-- ComponentMalfunction
        click ComponentMalfunction href "../ComponentMalfunction/"
      PotentialRiskSource <|-- CompromiseAccount
        click CompromiseAccount href "../CompromiseAccount/"
      PotentialRiskSource <|-- CompromiseAccountCredentials
        click CompromiseAccountCredentials href "../CompromiseAccountCredentials/"
      PotentialRiskSource <|-- ConfidentialityBreach
        click ConfidentialityBreach href "../ConfidentialityBreach/"
      PotentialRiskSource <|-- ConfirmationBias
        click ConfirmationBias href "../ConfirmationBias/"
      PotentialRiskSource <|-- ConfoundingVariablesBias
        click ConfoundingVariablesBias href "../ConfoundingVariablesBias/"
      PotentialRiskSource <|-- CoverageBias
        click CoverageBias href "../CoverageBias/"
      PotentialRiskSource <|-- Cryptojacking
        click Cryptojacking href "../Cryptojacking/"
      PotentialRiskSource <|-- DataAggregationBias
        click DataAggregationBias href "../DataAggregationBias/"
      PotentialRiskSource <|-- DataBias
        click DataBias href "../DataBias/"
      PotentialRiskSource <|-- DataBreach
        click DataBreach href "../DataBreach/"
      PotentialRiskSource <|-- DataCollectionError
        click DataCollectionError href "../DataCollectionError/"
      PotentialRiskSource <|-- DataCorruption
        click DataCorruption href "../DataCorruption/"
      PotentialRiskSource <|-- DataErasureError
        click DataErasureError href "../DataErasureError/"
      PotentialRiskSource <|-- DataInaccurate
        click DataInaccurate href "../DataInaccurate/"
      PotentialRiskSource <|-- DataIncomplete
        click DataIncomplete href "../DataIncomplete/"
      PotentialRiskSource <|-- DataInconsistent
        click DataInconsistent href "../DataInconsistent/"
      PotentialRiskSource <|-- DataLoss
        click DataLoss href "../DataLoss/"
      PotentialRiskSource <|-- DataMisclassified
        click DataMisclassified href "../DataMisclassified/"
      PotentialRiskSource <|-- DataMisinterpretation
        click DataMisinterpretation href "../DataMisinterpretation/"
      PotentialRiskSource <|-- DataNoise
        click DataNoise href "../DataNoise/"
      PotentialRiskSource <|-- DataOutdated
        click DataOutdated href "../DataOutdated/"
      PotentialRiskSource <|-- DataPreparationError
        click DataPreparationError href "../DataPreparationError/"
      PotentialRiskSource <|-- DataProcessingBias
        click DataProcessingBias href "../DataProcessingBias/"
      PotentialRiskSource <|-- DataProcessingError
        click DataProcessingError href "../DataProcessingError/"
      PotentialRiskSource <|-- DataRisk
        click DataRisk href "../DataRisk/"
      PotentialRiskSource <|-- DataSelectionError
        click DataSelectionError href "../DataSelectionError/"
      PotentialRiskSource <|-- DataSparse
        click DataSparse href "../DataSparse/"
      PotentialRiskSource <|-- DataStorageError
        click DataStorageError href "../DataStorageError/"
      PotentialRiskSource <|-- DataTransferError
        click DataTransferError href "../DataTransferError/"
      PotentialRiskSource <|-- DataUnavailable
        click DataUnavailable href "../DataUnavailable/"
      PotentialRiskSource <|-- DataUnrepresentative
        click DataUnrepresentative href "../DataUnrepresentative/"
      PotentialRiskSource <|-- DataUnstructured
        click DataUnstructured href "../DataUnstructured/"
      PotentialRiskSource <|-- DataUnverified
        click DataUnverified href "../DataUnverified/"
      PotentialRiskSource <|-- Deception
        click Deception href "../Deception/"
      PotentialRiskSource <|-- DenialServiceAttack
        click DenialServiceAttack href "../DenialServiceAttack/"
      PotentialRiskSource <|-- DistributedDenialServiceAttack
        click DistributedDenialServiceAttack href "../DistributedDenialServiceAttack/"
      PotentialRiskSource <|-- DocumentationIssues
        click DocumentationIssues href "../DocumentationIssues/"
      PotentialRiskSource <|-- EquipmentFailure
        click EquipmentFailure href "../EquipmentFailure/"
      PotentialRiskSource <|-- EquipmentMalfunction
        click EquipmentMalfunction href "../EquipmentMalfunction/"
      PotentialRiskSource <|-- ErroneousUse
        click ErroneousUse href "../ErroneousUse/"
      PotentialRiskSource <|-- Exploitation
        click Exploitation href "../Exploitation/"
      PotentialRiskSource <|-- ExternalSecurityThreat
        click ExternalSecurityThreat href "../ExternalSecurityThreat/"
      PotentialRiskSource <|-- Extortion
        click Extortion href "../Extortion/"
      PotentialRiskSource <|-- Fraud
        click Fraud href "../Fraud/"
      PotentialRiskSource <|-- GroupAttributionBias
        click GroupAttributionBias href "../GroupAttributionBias/"
      PotentialRiskSource <|-- HumanErrors
        click HumanErrors href "../HumanErrors/"
      PotentialRiskSource <|-- HumanOversightIneffective
        click HumanOversightIneffective href "../HumanOversightIneffective/"
      PotentialRiskSource <|-- HumanOversightInsufficient
        click HumanOversightInsufficient href "../HumanOversightInsufficient/"
      PotentialRiskSource <|-- IdentityFraud
        click IdentityFraud href "../IdentityFraud/"
      PotentialRiskSource <|-- IdentityTheft
        click IdentityTheft href "../IdentityTheft/"
      PotentialRiskSource <|-- ImplicitBias
        click ImplicitBias href "../ImplicitBias/"
      PotentialRiskSource <|-- InGroupBias
        click InGroupBias href "../InGroupBias/"
      PotentialRiskSource <|-- InformativenessBias
        click InformativenessBias href "../InformativenessBias/"
      PotentialRiskSource <|-- InstructionsInaccessible
        click InstructionsInaccessible href "../InstructionsInaccessible/"
      PotentialRiskSource <|-- InstructionsIncorrect
        click InstructionsIncorrect href "../InstructionsIncorrect/"
      PotentialRiskSource <|-- InstructionsInsufficient
        click InstructionsInsufficient href "../InstructionsInsufficient/"
      PotentialRiskSource <|-- InstructionsUnsuitable
        click InstructionsUnsuitable href "../InstructionsUnsuitable/"
      PotentialRiskSource <|-- IntegrityBreach
        click IntegrityBreach href "../IntegrityBreach/"
      PotentialRiskSource <|-- IntentionalManipulation
        click IntentionalManipulation href "../IntentionalManipulation/"
      PotentialRiskSource <|-- IntentionalMisuse
        click IntentionalMisuse href "../IntentionalMisuse/"
      PotentialRiskSource <|-- InterceptCommunications
        click InterceptCommunications href "../InterceptCommunications/"
      PotentialRiskSource <|-- LackOfSystemTransparency
        click LackOfSystemTransparency href "../LackOfSystemTransparency/"
      PotentialRiskSource <|-- LegalComplianceRisk
        click LegalComplianceRisk href "../LegalComplianceRisk/"
      PotentialRiskSource <|-- LegalRiskConcept
        click LegalRiskConcept href "../LegalRiskConcept/"
      PotentialRiskSource <|-- MaliciousActivity
        click MaliciousActivity href "../MaliciousActivity/"
      PotentialRiskSource <|-- MaliciousCodeAttack
        click MaliciousCodeAttack href "../MaliciousCodeAttack/"
      PotentialRiskSource <|-- MalwareAttack
        click MalwareAttack href "../MalwareAttack/"
      PotentialRiskSource <|-- Misuse
        click Misuse href "../Misuse/"
      PotentialRiskSource <|-- NonNormalityBias
        click NonNormalityBias href "../NonNormalityBias/"
      PotentialRiskSource <|-- NonResponseBias
        click NonResponseBias href "../NonResponseBias/"
      PotentialRiskSource <|-- OperationalSecurityRisk
        click OperationalSecurityRisk href "../OperationalSecurityRisk/"
      PotentialRiskSource <|-- OrganisationalManagementRisk
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      PotentialRiskSource <|-- OrganisationalRiskConcept
        click OrganisationalRiskConcept href "../OrganisationalRiskConcept/"
      PotentialRiskSource <|-- OutGroupHomogeneityBias
        click OutGroupHomogeneityBias href "../OutGroupHomogeneityBias/"
      PotentialRiskSource <|-- PhishingScam
        click PhishingScam href "../PhishingScam/"
      PotentialRiskSource <|-- PolicyRisk
        click PolicyRisk href "../PolicyRisk/"
      PotentialRiskSource <|-- QualityDegraded
        click QualityDegraded href "../QualityDegraded/"
      PotentialRiskSource <|-- QualityInconsistent
        click QualityInconsistent href "../QualityInconsistent/"
      PotentialRiskSource <|-- QualityInsufficient
        click QualityInsufficient href "../QualityInsufficient/"
      PotentialRiskSource <|-- QualityRisk
        click QualityRisk href "../QualityRisk/"
      PotentialRiskSource <|-- QualityUnknown
        click QualityUnknown href "../QualityUnknown/"
      PotentialRiskSource <|-- QualityUnverified
        click QualityUnverified href "../QualityUnverified/"
      PotentialRiskSource <|-- Reidentification
        click Reidentification href "../Reidentification/"
      PotentialRiskSource <|-- RequirementsBias
        click RequirementsBias href "../RequirementsBias/"
      PotentialRiskSource <|-- ResilienceDegraded
        click ResilienceDegraded href "../ResilienceDegraded/"
      PotentialRiskSource <|-- ResilienceInconsistent
        click ResilienceInconsistent href "../ResilienceInconsistent/"
      PotentialRiskSource <|-- ResilienceInsufficient
        click ResilienceInsufficient href "../ResilienceInsufficient/"
      PotentialRiskSource <|-- ResilienceRisk
        click ResilienceRisk href "../ResilienceRisk/"
      PotentialRiskSource <|-- ResilienceUnknown
        click ResilienceUnknown href "../ResilienceUnknown/"
      PotentialRiskSource <|-- ResilienceUnverified
        click ResilienceUnverified href "../ResilienceUnverified/"
      PotentialRiskSource <|-- RobustnessDegraded
        click RobustnessDegraded href "../RobustnessDegraded/"
      PotentialRiskSource <|-- RobustnessInconsistent
        click RobustnessInconsistent href "../RobustnessInconsistent/"
      PotentialRiskSource <|-- RobustnessInsufficient
        click RobustnessInsufficient href "../RobustnessInsufficient/"
      PotentialRiskSource <|-- RobustnessRisk
        click RobustnessRisk href "../RobustnessRisk/"
      PotentialRiskSource <|-- RobustnessUnknown
        click RobustnessUnknown href "../RobustnessUnknown/"
      PotentialRiskSource <|-- RobustnessUnverified
        click RobustnessUnverified href "../RobustnessUnverified/"
      PotentialRiskSource <|-- RuleBasedSystemDesign
        click RuleBasedSystemDesign href "../RuleBasedSystemDesign/"
      PotentialRiskSource <|-- Sabotage
        click Sabotage href "../Sabotage/"
      PotentialRiskSource <|-- SamplingBias
        click SamplingBias href "../SamplingBias/"
      PotentialRiskSource <|-- Scam
        click Scam href "../Scam/"
      PotentialRiskSource <|-- SecurityAttack
        click SecurityAttack href "../SecurityAttack/"
      PotentialRiskSource <|-- SecurityBreach
        click SecurityBreach href "../SecurityBreach/"
      PotentialRiskSource <|-- SecurityQualityDegraded
        click SecurityQualityDegraded href "../SecurityQualityDegraded/"
      PotentialRiskSource <|-- SecurityQualityInconsistent
        click SecurityQualityInconsistent href "../SecurityQualityInconsistent/"
      PotentialRiskSource <|-- SecurityQualityInsufficient
        click SecurityQualityInsufficient href "../SecurityQualityInsufficient/"
      PotentialRiskSource <|-- SecurityQualityRisk
        click SecurityQualityRisk href "../SecurityQualityRisk/"
      PotentialRiskSource <|-- SecurityQualityUnknown
        click SecurityQualityUnknown href "../SecurityQualityUnknown/"
      PotentialRiskSource <|-- SecurityQualityUnverified
        click SecurityQualityUnverified href "../SecurityQualityUnverified/"
      PotentialRiskSource <|-- SelectionBias
        click SelectionBias href "../SelectionBias/"
      PotentialRiskSource <|-- SimpsonsParadoxBias
        click SimpsonsParadoxBias href "../SimpsonsParadoxBias/"
      PotentialRiskSource <|-- SocietalBias
        click SocietalBias href "../SocietalBias/"
      PotentialRiskSource <|-- SocietalRiskConcept
        click SocietalRiskConcept href "../SocietalRiskConcept/"
      PotentialRiskSource <|-- Spoofing
        click Spoofing href "../Spoofing/"
      PotentialRiskSource <|-- StaffIncompetence
        click StaffIncompetence href "../StaffIncompetence/"
      PotentialRiskSource <|-- StatisticalBias
        click StatisticalBias href "../StatisticalBias/"
      PotentialRiskSource <|-- SystemFailure
        click SystemFailure href "../SystemFailure/"
      PotentialRiskSource <|-- SystemIntrusion
        click SystemIntrusion href "../SystemIntrusion/"
      PotentialRiskSource <|-- SystemMalfunction
        click SystemMalfunction href "../SystemMalfunction/"
      PotentialRiskSource <|-- TaskExecutionIncorrect
        click TaskExecutionIncorrect href "../TaskExecutionIncorrect/"
      PotentialRiskSource <|-- TaskExecutionRisk
        click TaskExecutionRisk href "../TaskExecutionRisk/"
      PotentialRiskSource <|-- TaskOmitted
        click TaskOmitted href "../TaskOmitted/"
      PotentialRiskSource <|-- TaskTimingIncorrect
        click TaskTimingIncorrect href "../TaskTimingIncorrect/"
      PotentialRiskSource <|-- TechnicalRiskConcept
        click TechnicalRiskConcept href "../TechnicalRiskConcept/"
      PotentialRiskSource <|-- TechnologyOverreliance
        click TechnologyOverreliance href "../TechnologyOverreliance/"
      PotentialRiskSource <|-- UnauthorisedAccessToPremises
        click UnauthorisedAccessToPremises href "../UnauthorisedAccessToPremises/"
      PotentialRiskSource <|-- UnauthorisedActivity
        click UnauthorisedActivity href "../UnauthorisedActivity/"
      PotentialRiskSource <|-- UnauthorisedCodeAccess
        click UnauthorisedCodeAccess href "../UnauthorisedCodeAccess/"
      PotentialRiskSource <|-- UnauthorisedCodeDisclosure
        click UnauthorisedCodeDisclosure href "../UnauthorisedCodeDisclosure/"
      PotentialRiskSource <|-- UnauthorisedCodeModification
        click UnauthorisedCodeModification href "../UnauthorisedCodeModification/"
      PotentialRiskSource <|-- UnauthorisedDataAccess
        click UnauthorisedDataAccess href "../UnauthorisedDataAccess/"
      PotentialRiskSource <|-- UnauthorisedDataDisclosure
        click UnauthorisedDataDisclosure href "../UnauthorisedDataDisclosure/"
      PotentialRiskSource <|-- UnauthorisedDataModification
        click UnauthorisedDataModification href "../UnauthorisedDataModification/"
      PotentialRiskSource <|-- UnauthorisedInformationDisclosure
        click UnauthorisedInformationDisclosure href "../UnauthorisedInformationDisclosure/"
      PotentialRiskSource <|-- UnauthorisedReidentification
        click UnauthorisedReidentification href "../UnauthorisedReidentification/"
      PotentialRiskSource <|-- UnauthorisedResourceUse
        click UnauthorisedResourceUse href "../UnauthorisedResourceUse/"
      PotentialRiskSource <|-- UnauthorisedSystemAccess
        click UnauthorisedSystemAccess href "../UnauthorisedSystemAccess/"
      PotentialRiskSource <|-- UnauthorisedSystemModification
        click UnauthorisedSystemModification href "../UnauthorisedSystemModification/"
      PotentialRiskSource <|-- UnwantedCodeDeletion
        click UnwantedCodeDeletion href "../UnwantedCodeDeletion/"
      PotentialRiskSource <|-- UnwantedDataDeletion
        click UnwantedDataDeletion href "../UnwantedDataDeletion/"
      PotentialRiskSource <|-- UnwantedDisclosureData
        click UnwantedDisclosureData href "../UnwantedDisclosureData/"
      PotentialRiskSource <|-- UserRisks
        click UserRisks href "../UserRisks/"
      PotentialRiskSource <|-- VulnerabilityExploitation
        click VulnerabilityExploitation href "../VulnerabilityExploitation/"
      
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:PotentialRiskSource](https://w3id.org/lmodel/dpv/risk/PotentialRiskSource) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Potential RiskSource


## Comments

* PotentialRiskSource is a suggestion that the concept can be a 'risk'
within an use-case - this suggestion is not exclusive and the concept
may also be instances of other potential concepts to indicate the
multiple possible roles a concept can take. This suggestion can be
ignored if it is not applicable to the use-case



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#PotentialRiskSource |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:PotentialRiskSource |
| native | risk:PotentialRiskSource |
| exact | dpv_risk:PotentialRiskSource, dpv_risk_owl:PotentialRiskSource |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PotentialRiskSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PotentialRiskSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates a concept can potentially be a ''risk source'' concept within
  an

  use-case'
comments:
- 'PotentialRiskSource is a suggestion that the concept can be a ''risk''

  within an use-case - this suggestion is not exclusive and the concept

  may also be instances of other potential concepts to indicate the

  multiple possible roles a concept can take. This suggestion can be

  ignored if it is not applicable to the use-case'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Potential RiskSource
exact_mappings:
- dpv_risk:PotentialRiskSource
- dpv_risk_owl:PotentialRiskSource
class_uri: risk:PotentialRiskSource

```
</details>

### Induced

<details>
```yaml
name: PotentialRiskSource
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#PotentialRiskSource
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Indicates a concept can potentially be a ''risk source'' concept within
  an

  use-case'
comments:
- 'PotentialRiskSource is a suggestion that the concept can be a ''risk''

  within an use-case - this suggestion is not exclusive and the concept

  may also be instances of other potential concepts to indicate the

  multiple possible roles a concept can take. This suggestion can be

  ignored if it is not applicable to the use-case'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Potential RiskSource
exact_mappings:
- dpv_risk:PotentialRiskSource
- dpv_risk_owl:PotentialRiskSource
class_uri: risk:PotentialRiskSource

```
</details></div>