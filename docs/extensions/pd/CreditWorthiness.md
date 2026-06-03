---
search:
  boost: 10.0
---

# Class: CreditWorthiness 


_Information about credit worthiness_



<div data-search-exclude markdown="1">



URI: [pd:CreditWorthiness](https://w3id.org/lmodel/dpv/pd/CreditWorthiness)





```mermaid
 classDiagram
    class CreditWorthiness
    click CreditWorthiness href "../CreditWorthiness/"
      Credit <|-- CreditWorthiness
        click Credit href "../Credit/"
      

      CreditWorthiness <|-- CreditScore
        click CreditScore href "../CreditScore/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * [Credit](Credit.md)
            * **CreditWorthiness**
                * [CreditScore](CreditScore.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CreditWorthiness](https://w3id.org/lmodel/dpv/pd/CreditWorthiness) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Credit Worthiness




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CreditWorthiness |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CreditWorthiness |
| native | pd:CreditWorthiness |
| exact | dpv_pd:CreditWorthiness, dpv_pd_owl:CreditWorthiness |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CreditWorthiness
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditWorthiness
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit worthiness
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Worthiness
exact_mappings:
- dpv_pd:CreditWorthiness
- dpv_pd_owl:CreditWorthiness
is_a: Credit
class_uri: pd:CreditWorthiness

```
</details>

### Induced

<details>
```yaml
name: CreditWorthiness
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditWorthiness
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit worthiness
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Worthiness
exact_mappings:
- dpv_pd:CreditWorthiness
- dpv_pd_owl:CreditWorthiness
is_a: Credit
class_uri: pd:CreditWorthiness

```
</details></div>