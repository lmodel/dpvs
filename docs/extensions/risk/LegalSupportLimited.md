---
search:
  boost: 10.0
---

# Class: LegalSupportLimited 


_Concept representing limitation of legal support_



<div data-search-exclude markdown="1">



URI: [risk:LegalSupportLimited](https://w3id.org/lmodel/dpv/risk/LegalSupportLimited)





```mermaid
 classDiagram
    class LegalSupportLimited
    click LegalSupportLimited href "../LegalSupportLimited/"
      PotentialConsequence <|-- LegalSupportLimited
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- LegalSupportLimited
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- LegalSupportLimited
        click PotentialRisk href "../PotentialRisk/"
      ServiceRelatedConsequence <|-- LegalSupportLimited
        click ServiceRelatedConsequence href "../ServiceRelatedConsequence/"
      
      
```





## Inheritance
* [OrganisationalRiskConcept](OrganisationalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [ServiceRelatedConsequence](ServiceRelatedConsequence.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **LegalSupportLimited** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:LegalSupportLimited](https://w3id.org/lmodel/dpv/risk/LegalSupportLimited) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Legal Support Limited




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#LegalSupportLimited |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:LegalSupportLimited |
| native | risk:LegalSupportLimited |
| exact | dpv_risk:LegalSupportLimited, dpv_risk_owl:LegalSupportLimited |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LegalSupportLimited
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegalSupportLimited
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing limitation of legal support
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legal Support Limited
exact_mappings:
- dpv_risk:LegalSupportLimited
- dpv_risk_owl:LegalSupportLimited
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LegalSupportLimited

```
</details>

### Induced

<details>
```yaml
name: LegalSupportLimited
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#LegalSupportLimited
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: Concept representing limitation of legal support
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Legal Support Limited
exact_mappings:
- dpv_risk:LegalSupportLimited
- dpv_risk_owl:LegalSupportLimited
is_a: ServiceRelatedConsequence
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:LegalSupportLimited

```
</details></div>