---
search:
  boost: 10.0
---

# Class: Damage 


_Concept representing Damage_



<div data-search-exclude markdown="1">



URI: [risk:Damage](https://w3id.org/lmodel/dpv/risk/Damage)





```mermaid
 classDiagram
    class Damage
    click Damage href "../Damage/"
      PotentialConsequence <|-- Damage
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- Damage
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- Damage
        click PotentialRisk href "../PotentialRisk/"
      LegallyRelevantConsequence <|-- Damage
        click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegallyRelevantConsequence](LegallyRelevantConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **Damage** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:Damage](https://w3id.org/lmodel/dpv/risk/Damage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Damage




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#Damage |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:Damage |
| native | risk:Damage |
| exact | dpv_risk:Damage, dpv_risk_owl:Damage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Damage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Damage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Damage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Damage
exact_mappings:
- dpv_risk:Damage
- dpv_risk_owl:Damage
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Damage

```
</details>

### Induced

<details>
```yaml
name: Damage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#Damage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Damage
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Damage
exact_mappings:
- dpv_risk:Damage
- dpv_risk_owl:Damage
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:Damage

```
</details></div>