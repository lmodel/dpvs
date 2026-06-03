---
search:
  boost: 10.0
---

# Class: LackOfSystemTransparency 


_Concept representing lack of transparency to humans related to the_

_operation of a system_



<div data-search-exclude markdown="1">



URI: [risk:LackOfSystemTransparency](https://w3id.org/lmodel/dpv/risk/LackOfSystemTransparency)





```mermaid
 classDiagram
    class LackOfSystemTransparency
    click LackOfSystemTransparency href "../LackOfSystemTransparency/"
      PotentialConsequence <|-- LackOfSystemTransparency
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialRisk <|-- LackOfSystemTransparency
        click PotentialRisk href "../PotentialRisk/"
      PotentialRiskSource <|-- LackOfSystemTransparency
        click PotentialRiskSource href "../PotentialRiskSource/"
      OrganisationalManagementRisk <|-- LackOfSystemTransparency
        click OrganisationalManagementRisk href "../OrganisationalManagementRisk/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [OrganisationalManagementRisk](OrganisationalManagementRisk.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
        * **LackOfSystemTransparency** [ [PotentialConsequence](PotentialConsequence.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LackOfSystemTransparency](https://w3id.org/lmodel/dpv/risk/LackOfSystemTransparency) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Lack Of System Transparency




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LackOfSystemTransparency |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LackOfSystemTransparency |
| native | risk:LackOfSystemTransparency |
| exact | dpv_risk:LackOfSystemTransparency, dpv_risk_owl:LackOfSystemTransparency |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LackOfSystemTransparency
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LackOfSystemTransparency
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing lack of transparency to humans related to the

  operation of a system'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Lack Of System Transparency
exact_mappings:
- dpv_risk:LackOfSystemTransparency
- dpv_risk_owl:LackOfSystemTransparency
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:LackOfSystemTransparency

```
</details>

### Induced

<details>
```yaml
name: LackOfSystemTransparency
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LackOfSystemTransparency
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Concept representing lack of transparency to humans related to the

  operation of a system'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Lack Of System Transparency
exact_mappings:
- dpv_risk:LackOfSystemTransparency
- dpv_risk_owl:LackOfSystemTransparency
is_a: OrganisationalManagementRisk
mixins:
- PotentialConsequence
- PotentialRisk
- PotentialRiskSource
class_uri: risk:LackOfSystemTransparency

```
</details></div>