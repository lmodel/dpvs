# DPV - Justifications

LinkML schema generated from the DPV 2.3 extension `justifications`
(`justifications-owl.ttl`), enriched with canonical SKOS metadata.
Imports the semantic-group schema(s) `dpv:schema/dpv_common` for the
abstract parent classes this extension specialises (instead of the full
umbrella `dpv:schema/dpv`).

URI: https://w3id.org/lmodel/dpv/justifications

Name: dpv_justifications



## Classes

| Class | Description |
| --- | --- |
| [DelayJustification](DelayJustification.md) | Justification to delay a process |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComplexityOfProcess](ComplexityOfProcess.md) | Justification that the process is delayed due to complexity in |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HighVolumeOfProcesses](HighVolumeOfProcesses.md) | Justification that the process is delayed due to high volume of similar |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IdentityVerificationRequired](IdentityVerificationRequired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InformationRequired](InformationRequired.md) | Justification that the process is delayed due to additional information |
| [ExerciseJustification](ExerciseJustification.md) | Justification for why the process should be carried out |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[InformationSocietyServicesOffer](InformationSocietyServicesOffer.md) | Justification that the process should be carried out due to it being |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalObligation](LegalObligation.md) | Justification that the process should be carried out due to it being a |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Objection](Objection.md) | Justification that the process should be carried out due to specified |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContestAccuracy](ContestAccuracy.md) | Justification that the process should be carried out due it being an |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalityLackingObjection](LegalityLackingObjection.md) | Justification that the process should be carried out due to it being an |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NonNecessityObjection](NonNecessityObjection.md) | Justification that the process should be carried out due to it being an |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UnlawfulActivityObjection](UnlawfulActivityObjection.md) | Justification that the process should be carried out due to it being an |
| [NonFulfilmentJustification](NonFulfilmentJustification.md) | Justification for not fulfilling a process or requirement or obligation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConsentProvided](ConsentProvided.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DisproportionateEffortRequired](DisproportionateEffortRequired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EntityAlreadyInformed](EntityAlreadyInformed.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EthicsProcedureImpaired](EthicsProcedureImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EthicsBreachDetectionImpaired](EthicsBreachDetectionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EthicsBreachInvestigationImpaired](EthicsBreachInvestigationImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EthicsBreachPreventionImpaired](EthicsBreachPreventionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EthicsBreachProsecutionImpaired](EthicsBreachProsecutionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FulfilmentImpossible](FulfilmentImpossible.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LackOfIntent](LackOfIntent.md) | Justification that the process could not be fulfilled as the requestor |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalProcessImpaired](LegalProcessImpaired.md) | Justification that the process could not be fulfilled as it impairs or |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CivilLawEnforcementImpaired](CivilLawEnforcementImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConfidentialityObligationCompromised](ConfidentialityObligationCompromised.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContractEstablishmentNecessity](ContractEstablishmentNecessity.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ContractPerformanceNecessity](ContractPerformanceNecessity.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrimeDetectionImpaired](CrimeDetectionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrimeInvestigationImpaired](CrimeInvestigationImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrimePenaltyExecutionImpaired](CrimePenaltyExecutionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrimePreventionImpaired](CrimePreventionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CrimeProsecutionImpaired](CrimeProsecutionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataSubjectProtectionImpaired](DataSubjectProtectionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DefenceImpaired](DefenceImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FreedomOfExpressionImpaired](FreedomOfExpressionImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IdentityVerificationFailure](IdentityVerificationFailure.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[JudicialProceedingsImpaired](JudicialProceedingsImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalClaimImpaired](LegalClaimImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalClaimDefenceImpaired](LegalClaimDefenceImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalClaimEstablishmentImpaired](LegalClaimEstablishmentImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalClaimExerciseImpaired](LegalClaimExerciseImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegallyExempted](LegallyExempted.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegalObligationImpaired](LegalObligationImpaired.md) | Justification that the process could not be fulfilled as it would impair |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NationalSecurityImpaired](NationalSecurityImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OfficialAuthorityExerciseImpaired](OfficialAuthorityExerciseImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OfficialStatisticsImpaired](OfficialStatisticsImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PublicHealthCompromised](PublicHealthCompromised.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PublicInterestArchivingImpaired](PublicInterestArchivingImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PublicInterestCompromised](PublicInterestCompromised.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PublicSecurityImpaired](PublicSecurityImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ThirdPartyRightsImpaired](ThirdPartyRightsImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LegitimateInterestOverride](LegitimateInterestOverride.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ObjectivesImpaired](ObjectivesImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessRejected](ProcessRejected.md) | Justification that the process could not be fulfilled because of one of |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessExcessive](ProcessExcessive.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessFrivolous](ProcessFrivolous.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessMalicious](ProcessMalicious.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessUnfounded](ProcessUnfounded.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ScientificHistoricalResearchImpaired](ScientificHistoricalResearchImpaired.md) | Justification that the process could not be fulfilled or was not |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SecurityImpaired](SecurityImpaired.md) | Justification that the process could not be fulfilled or was not |
| [NotRequiredJustification](NotRequiredJustification.md) | Justification to reject or not complete a process as it is not required |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProcessSafeguarded](ProcessSafeguarded.md) | Justification that the process is not required as it is safeguarded by |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RightsFreedomsImpactUnlikely](RightsFreedomsImpactUnlikely.md) | Justification that the process is not required as it is considered to be |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RiskMitigated](RiskMitigated.md) | Justification that the process is not required as the risks have been |



## Slots

| Slot | Description |
| --- | --- |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
| [JustificationsJustificationsDelaySubset](JustificationsJustificationsDelaySubset.md) | Entities from the DPV `justifications/modules/justifications_delay` |
| [JustificationsJustificationsExerciseSubset](JustificationsJustificationsExerciseSubset.md) | Entities from the DPV `justifications/modules/justifications_exercise` |
| [JustificationsJustificationsNonfulfilmentSubset](JustificationsJustificationsNonfulfilmentSubset.md) | Entities from the DPV |
| [JustificationsJustificationsNotrequiredSubset](JustificationsJustificationsNotrequiredSubset.md) | Entities from the DPV |
| [JustificationsSubset](JustificationsSubset.md) | All entities from the DPV `justifications` extension |
