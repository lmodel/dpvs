---
search:
  boost: 10.0
---

# Class: Detriment 


_Concept representing Detriment_



<div data-search-exclude markdown="1">



URI: [risk:Detriment](https://w3id.org/lmodel/dpv/risk/Detriment)





```mermaid
 classDiagram
    class Detriment
    click Detriment href "../Detriment/"
      PotentialConsequence <|-- Detriment
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Detriment
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Detriment
        click PotentialRisk href "../PotentialRisk/"
      LegallyRelevantConsequence <|-- Detriment
        click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegallyRelevantConsequence](LegallyRelevantConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Detriment** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Detriment](https://w3id.org/lmodel/dpv/risk/Detriment) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Detriment




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Detriment |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Detriment |
| native | risk:Detriment |
| exact | dpv_risk:Detriment, dpv_risk_owl:Detriment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Detriment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Detriment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Detriment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Detriment
exact_mappings:
- dpv_risk:Detriment
- dpv_risk_owl:Detriment
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Detriment

```
</details>

### Induced

<details>
```yaml
name: Detriment
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Detriment
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Detriment
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Detriment
exact_mappings:
- dpv_risk:Detriment
- dpv_risk_owl:Detriment
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Detriment

```
</details></div>