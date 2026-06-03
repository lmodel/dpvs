---
search:
  boost: 10.0
---

# Class: CreditCapacity 


_Information about credit capacity_



<div data-search-exclude markdown="1">



URI: [pd:CreditCapacity](https://w3id.org/lmodel/dpv/pd/CreditCapacity)





```mermaid
 classDiagram
    class CreditCapacity
    click CreditCapacity href "../CreditCapacity/"
      Credit <|-- CreditCapacity
        click Credit href "../Credit/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * [Credit](Credit.md)
            * **CreditCapacity**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CreditCapacity](https://w3id.org/lmodel/dpv/pd/CreditCapacity) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Credit Capacity




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CreditCapacity |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CreditCapacity |
| native | pd:CreditCapacity |
| exact | dpv_pd:CreditCapacity, dpv_pd_owl:CreditCapacity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CreditCapacity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditCapacity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit capacity
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Capacity
exact_mappings:
- dpv_pd:CreditCapacity
- dpv_pd_owl:CreditCapacity
is_a: Credit
class_uri: pd:CreditCapacity

```
</details>

### Induced

<details>
```yaml
name: CreditCapacity
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditCapacity
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit capacity
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Capacity
exact_mappings:
- dpv_pd:CreditCapacity
- dpv_pd_owl:CreditCapacity
is_a: Credit
class_uri: pd:CreditCapacity

```
</details></div>