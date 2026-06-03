---
search:
  boost: 10.0
---

# Class: LoanRecord 


_Information about loans, whether applied, provided or rejected, and its_

_history_



<div data-search-exclude markdown="1">



URI: [pd:LoanRecord](https://w3id.org/lmodel/dpv/pd/LoanRecord)





```mermaid
 classDiagram
    class LoanRecord
    click LoanRecord href "../LoanRecord/"
      Transactional <|-- LoanRecord
        click Transactional href "../Transactional/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Transactional](Transactional.md)
        * **LoanRecord**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:LoanRecord](https://w3id.org/lmodel/dpv/pd/LoanRecord) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Loan Record




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#LoanRecord |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:LoanRecord |
| native | pd:LoanRecord |
| exact | dpv_pd:LoanRecord, dpv_pd_owl:LoanRecord |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LoanRecord
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#LoanRecord
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about loans, whether applied, provided or rejected, and
  its

  history'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Loan Record
exact_mappings:
- dpv_pd:LoanRecord
- dpv_pd_owl:LoanRecord
is_a: Transactional
class_uri: pd:LoanRecord

```
</details>

### Induced

<details>
```yaml
name: LoanRecord
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#LoanRecord
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about loans, whether applied, provided or rejected, and
  its

  history'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Loan Record
exact_mappings:
- dpv_pd:LoanRecord
- dpv_pd_owl:LoanRecord
is_a: Transactional
class_uri: pd:LoanRecord

```
</details></div>