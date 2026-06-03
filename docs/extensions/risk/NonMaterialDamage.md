---
search:
  boost: 10.0
---

# Class: NonMaterialDamage 


_Concept representing Non-Material Damage_



<div data-search-exclude markdown="1">



URI: [risk:NonMaterialDamage](https://w3id.org/lmodel/dpv/risk/NonMaterialDamage)





```mermaid
 classDiagram
    class NonMaterialDamage
    click NonMaterialDamage href "../NonMaterialDamage/"
      PotentialConsequence <|-- NonMaterialDamage
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- NonMaterialDamage
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- NonMaterialDamage
        click PotentialRisk href "../PotentialRisk/"
      LegallyRelevantConsequence <|-- NonMaterialDamage
        click LegallyRelevantConsequence href "../LegallyRelevantConsequence/"
      
      
```





## Inheritance
* [LegalRiskConcept](LegalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [LegallyRelevantConsequence](LegallyRelevantConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **NonMaterialDamage** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:NonMaterialDamage](https://w3id.org/lmodel/dpv/risk/NonMaterialDamage) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Non-Material Damage


## Comments

* The criteria for what is considered material damage is based in
jurisdictional laws and norms



## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#NonMaterialDamage |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:NonMaterialDamage |
| native | risk:NonMaterialDamage |
| exact | dpv_risk:NonMaterialDamage, dpv_risk_owl:NonMaterialDamage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NonMaterialDamage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NonMaterialDamage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Non-Material Damage
comments:
- 'The criteria for what is considered material damage is based in

  jurisdictional laws and norms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Non-Material Damage
exact_mappings:
- dpv_risk:NonMaterialDamage
- dpv_risk_owl:NonMaterialDamage
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:NonMaterialDamage

```
</details>

### Induced

<details>
```yaml
name: NonMaterialDamage
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#NonMaterialDamage
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing Non-Material Damage
comments:
- 'The criteria for what is considered material damage is based in

  jurisdictional laws and norms'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Non-Material Damage
exact_mappings:
- dpv_risk:NonMaterialDamage
- dpv_risk_owl:NonMaterialDamage
is_a: LegallyRelevantConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:NonMaterialDamage

```
</details></div>