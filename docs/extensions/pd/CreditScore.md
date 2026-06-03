---
search:
  boost: 10.0
---

# Class: CreditScore 


_Information about credit score_



<div data-search-exclude markdown="1">



URI: [pd:CreditScore](https://w3id.org/lmodel/dpv/pd/CreditScore)





```mermaid
 classDiagram
    class CreditScore
    click CreditScore href "../CreditScore/"
      CreditWorthiness <|-- CreditScore
        click CreditWorthiness href "../CreditWorthiness/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * [Credit](Credit.md)
            * [CreditWorthiness](CreditWorthiness.md)
                * **CreditScore**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CreditScore](https://w3id.org/lmodel/dpv/pd/CreditScore) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Credit Score




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CreditScore |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CreditScore |
| native | pd:CreditScore |
| exact | dpv_pd:CreditScore, dpv_pd_owl:CreditScore |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CreditScore
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditScore
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit score
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Score
exact_mappings:
- dpv_pd:CreditScore
- dpv_pd_owl:CreditScore
is_a: CreditWorthiness
class_uri: pd:CreditScore

```
</details>

### Induced

<details>
```yaml
name: CreditScore
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditScore
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit score
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Score
exact_mappings:
- dpv_pd:CreditScore
- dpv_pd_owl:CreditScore
is_a: CreditWorthiness
class_uri: pd:CreditScore

```
</details></div>