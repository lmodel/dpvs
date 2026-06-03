---
search:
  boost: 10.0
---

# Class: ExcellenceDiscrimination 


_Favouritism towards individuals deemed more competent or superior, often_

_at the expense of others_



<div data-search-exclude markdown="1">



URI: [risk:ExcellenceDiscrimination](https://w3id.org/lmodel/dpv/risk/ExcellenceDiscrimination)





```mermaid
 classDiagram
    class ExcellenceDiscrimination
    click ExcellenceDiscrimination href "../ExcellenceDiscrimination/"
      PotentialConsequence <|-- ExcellenceDiscrimination
        click PotentialConsequence href "../PotentialConsequence/"
      PotentialImpact <|-- ExcellenceDiscrimination
        click PotentialImpact href "../PotentialImpact/"
      PotentialRisk <|-- ExcellenceDiscrimination
        click PotentialRisk href "../PotentialRisk/"
      Discrimination <|-- ExcellenceDiscrimination
        click Discrimination href "../Discrimination/"
      
      
```





## Inheritance
* [SocietalRiskConcept](SocietalRiskConcept.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md) [PotentialRiskSource](PotentialRiskSource.md)]
    * [Discrimination](Discrimination.md) [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]
        * **ExcellenceDiscrimination** [ [PotentialConsequence](PotentialConsequence.md) [PotentialImpact](PotentialImpact.md) [PotentialRisk](PotentialRisk.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [risk:ExcellenceDiscrimination](https://w3id.org/lmodel/dpv/risk/ExcellenceDiscrimination) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [RiskSubset](RiskSubset.md)



## Aliases


* Excellence Discrimination




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/risk/owl#ExcellenceDiscrimination |
| dpv_extension_slug | risk |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/risk




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | risk:ExcellenceDiscrimination |
| native | risk:ExcellenceDiscrimination |
| exact | dpv_risk:ExcellenceDiscrimination, dpv_risk_owl:ExcellenceDiscrimination |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExcellenceDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExcellenceDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Favouritism towards individuals deemed more competent or superior, often

  at the expense of others'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Excellence Discrimination
exact_mappings:
- dpv_risk:ExcellenceDiscrimination
- dpv_risk_owl:ExcellenceDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ExcellenceDiscrimination

```
</details>

### Induced

<details>
```yaml
name: ExcellenceDiscrimination
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/risk/owl#ExcellenceDiscrimination
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: risk
description: 'Favouritism towards individuals deemed more competent or superior, often

  at the expense of others'
in_subset:
- risk_subset
from_schema: https://w3id.org/lmodel/dpv/risk
aliases:
- Excellence Discrimination
exact_mappings:
- dpv_risk:ExcellenceDiscrimination
- dpv_risk_owl:ExcellenceDiscrimination
is_a: Discrimination
mixins:
- PotentialConsequence
- PotentialImpact
- PotentialRisk
class_uri: risk:ExcellenceDiscrimination

```
</details></div>