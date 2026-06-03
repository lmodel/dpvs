---
search:
  boost: 10.0
---

# Class: Misuse 


_Concept representing a misuse (of something)_



<div data-search-exclude markdown="1">



URI: [risk:Misuse](https://w3id.org/lmodel/dpv/risk/Misuse)





```mermaid
 classDiagram
    class Misuse
    click Misuse href "../Misuse/"
      PotentialConsequence <|-- Misuse
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- Misuse
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- Misuse
        click PotentialRiskSource href "../PotentialRiskSource/"
      UserRisks <|-- Misuse
        click UserRisks href "../UserRisks/"
      

      Misuse <|-- AccidentalMisuse
        click AccidentalMisuse href "../AccidentalMisuse/"
      Misuse <|-- IntentionalMisuse
        click IntentionalMisuse href "../IntentionalMisuse/"
      

      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [UserRisks](UserRisks.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **Misuse** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [AccidentalMisuse](AccidentalMisuse.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
            * [IntentionalMisuse](IntentionalMisuse.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Misuse](https://w3id.org/lmodel/dpv/risk/Misuse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Misuse




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Misuse |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Misuse |
| native | risk:Misuse |
| exact | dpv_risk:Misuse, dpv_risk_owl:Misuse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Misuse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Misuse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing a misuse (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Misuse
exact_mappings:
- dpv_risk:Misuse
- dpv_risk_owl:Misuse
is_a: UserRisks
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Misuse

```
</details>

### Induced

<details>
```yaml
name: Misuse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Misuse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing a misuse (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Misuse
exact_mappings:
- dpv_risk:Misuse
- dpv_risk_owl:Misuse
is_a: UserRisks
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:Misuse

```
</details></div>