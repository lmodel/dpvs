---
search:
  boost: 10.0
---

# Class: MaterialDamage 


_Concept representing Material Damage_



<div data-search-exclude markdown="1">



URI: [risk:MaterialDamage](https://w3id.org/lmodel/dpv/risk/MaterialDamage)





```mermaid
 classDiagram
    class MaterialDamage
    click MaterialDamage href "../MaterialDamage/"
      PotentialConsequence <|-- MaterialDamage
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- MaterialDamage
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- MaterialDamage
        click PotentialRisk href "../PotentialRisk/"
      LegallyRelevantConsequence <|-- MaterialDamage
        click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegallyRelevantConsequence](LegallyRelevantConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **MaterialDamage** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:MaterialDamage](https://w3id.org/lmodel/dpv/risk/MaterialDamage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Material Damage


## Comments

* The criteria for what is considered material damage is based in
jurisdictional laws and norms



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#MaterialDamage |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:MaterialDamage |
| native | risk:MaterialDamage |
| exact | dpv_risk:MaterialDamage, dpv_risk_owl:MaterialDamage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MaterialDamage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MaterialDamage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Material Damage
comments:
- 'The criteria for what is considered material damage is based in

  jurisdictional laws and norms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Material Damage
exact_mappings:
- dpv_risk:MaterialDamage
- dpv_risk_owl:MaterialDamage
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:MaterialDamage

```
</details>

### Induced

<details>
```yaml
name: MaterialDamage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#MaterialDamage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Material Damage
comments:
- 'The criteria for what is considered material damage is based in

  jurisdictional laws and norms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Material Damage
exact_mappings:
- dpv_risk:MaterialDamage
- dpv_risk_owl:MaterialDamage
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:MaterialDamage

```
</details></div>