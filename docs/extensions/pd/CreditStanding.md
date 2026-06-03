---
search:
  boost: 10.0
---

# Class: CreditStanding 


_Information about credit standing_



<div data-search-exclude markdown="1">



URI: [pd:CreditStanding](https://w3id.org/lmodel/dpv/pd/CreditStanding)





```mermaid
 classDiagram
    class CreditStanding
    click CreditStanding href "../CreditStanding/"
      Credit <|-- CreditStanding
        click Credit href "../Credit/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * [Credit](Credit.md)
            * **CreditStanding**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CreditStanding](https://w3id.org/lmodel/dpv/pd/CreditStanding) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Credit Standing




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CreditStanding |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CreditStanding |
| native | pd:CreditStanding |
| exact | dpv_pd:CreditStanding, dpv_pd_owl:CreditStanding |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CreditStanding
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditStanding
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit standing
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Standing
exact_mappings:
- dpv_pd:CreditStanding
- dpv_pd_owl:CreditStanding
is_a: Credit
class_uri: pd:CreditStanding

```
</details>

### Induced

<details>
```yaml
name: CreditStanding
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditStanding
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit standing
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Standing
exact_mappings:
- dpv_pd:CreditStanding
- dpv_pd_owl:CreditStanding
is_a: Credit
class_uri: pd:CreditStanding

```
</details></div>