---
search:
  boost: 10.0
---

# Class: ErroneousUse 


_Concept representing erroneous use (of something)_



<div data-search-exclude markdown="1">



URI: [risk:ErroneousUse](https://w3id.org/lmodel/dpv/risk/ErroneousUse)





```mermaid
 classDiagram
    class ErroneousUse
    click ErroneousUse href "../ErroneousUse/"
      PotentialConsequence <|-- ErroneousUse
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- ErroneousUse
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- ErroneousUse
        click PotentialRiskSource href "../PotentialRiskSource/"
      UserRisks <|-- ErroneousUse
        click UserRisks href "../UserRisks/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [UserRisks](UserRisks.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **ErroneousUse** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ErroneousUse](https://w3id.org/lmodel/dpv/risk/ErroneousUse) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Erroneous Use




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ErroneousUse |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ErroneousUse |
| native | risk:ErroneousUse |
| exact | dpv_risk:ErroneousUse, dpv_risk_owl:ErroneousUse |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ErroneousUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ErroneousUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing erroneous use (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Erroneous Use
exact_mappings:
- dpv_risk:ErroneousUse
- dpv_risk_owl:ErroneousUse
is_a: UserRisks
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ErroneousUse

```
</details>

### Induced

<details>
```yaml
name: ErroneousUse
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ErroneousUse
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing erroneous use (of something)
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Erroneous Use
exact_mappings:
- dpv_risk:ErroneousUse
- dpv_risk_owl:ErroneousUse
is_a: UserRisks
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:ErroneousUse

```
</details></div>