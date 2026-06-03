---
search:
  boost: 10.0
---

# Class: CreditRecord 


_Information about credit record_



<div data-search-exclude markdown="1">



URI: [pd:CreditRecord](https://w3id.org/lmodel/dpv/pd/CreditRecord)





```mermaid
 classDiagram
    class CreditRecord
    click CreditRecord href "../CreditRecord/"
      Credit <|-- CreditRecord
        click Credit href "../Credit/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * [Credit](Credit.md)
            * **CreditRecord**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CreditRecord](https://w3id.org/lmodel/dpv/pd/CreditRecord) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Credit Record




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CreditRecord |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CreditRecord |
| native | pd:CreditRecord |
| exact | dpv_pd:CreditRecord, dpv_pd_owl:CreditRecord |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CreditRecord
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditRecord
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit record
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Record
exact_mappings:
- dpv_pd:CreditRecord
- dpv_pd_owl:CreditRecord
is_a: Credit
class_uri: pd:CreditRecord

```
</details>

### Induced

<details>
```yaml
name: CreditRecord
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CreditRecord
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about credit record
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Credit Record
exact_mappings:
- dpv_pd:CreditRecord
- dpv_pd_owl:CreditRecord
is_a: Credit
class_uri: pd:CreditRecord

```
</details></div>